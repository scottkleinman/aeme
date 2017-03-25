# Python imports
import os, re, json

# Import flask and template operators
from flask import Flask, render_template, request

# Other imports
from lxml import etree, html

# App imports
import managers.metadata
#import language.LANG_AEME as LANG
# Convert the module variables to a JSON string to send to the template
#language = json.dumps({key: value for key, value in LANG.__dict__.iteritems() if not (key.startswith('__') or key.startswith('_') or key.islower())})

# Define the WSGI application object
app = Flask(__name__)
#app = Flask(__name__, instance_relative_config=True)
application = app # our hosting requires application in passenger_wsgi

# Configurations
from ordbok.flask_helper import FlaskOrdbok

ordbok = FlaskOrdbok(app)
ordbok.load()
app.config.update(ordbok)

 # Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Build Menu
def buildMenu():
	config = app.config
	site = config["SITE_URL"]
	menu = config["MENU"]
	menu_str = '<ul id="menu-list" class="nav navbar-nav">'
	menu_str += '<li><a href="'+site+'">Home <span class="sr-only">(current)</span></a></li>'
	menu_str += """
       <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">About <span class="caret"></span></a>
          <ul class="dropdown-menu">
	"""
	menu_str += '<li><a href="'+site+'/about">About AEME</a></li>'
	menu_str += '<li><a href="'+site+'/guidelines">Transcription Guidelines</a></li>'
	menu_str += '<li><a href="'+site+'/downloads">Downloads</a></li>'
	menu_str += '<li><a href="'+site+'/credits">Credits</a></li>'
	menu_str += """
          </ul>
        </li>
	"""

	for item in menu:
		if type(item) is dict:
			for label, subitems in item.iteritems():
				dropdown ='<li class="dropdown">'
				dropdown += '<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">'
				dropdown += label + ' <span class="caret"></span></a>'
				dropdown += '<ul class="dropdown-menu">'
				for subitem in subitems:
				    dropdown += "<li>" + subitem + "</li>"
				dropdown += '</ul>'
				dropdown += '</li>'
				menu_str += dropdown
		else:
			menu_str += "<li>" + item + "</li>"
	menu_str += '</ul>'
	return menu_str

# Strip namespaces
def strip_ns(tree):
    for node in tree.iter():
        try:
            has_namespace = node.tag.startswith('{')
        except AttributeError:
            continue  # node.tag is not a string (node is a comment or similar)
        if has_namespace:
            node.tag = node.tag.split('}', 1)[1]
    return tree

# Re-format Notes
def reformat_notes(doc):
	for element in doc.iter(tag="tei-note"):
		text = element.text
		element.text = ""
		element.attrib["class"] = "note"
		element.attrib["data-content"] = text
		i = etree.Element("i")
		i.attrib["class"] = "fa fa-comment-o"
		element.insert(0, i)
	return doc

# Create spans for critical and diplomatic punctuation
def replace_pointing(doc):
	for element in doc.iter(tag="tei-pc"):
		c = element.text
		element.text = ""
		span1 = etree.Element("span")
		span1.text = c
		span1.attrib["class"] = "dip"
		element.insert(0, span1)
		span2 = etree.Element("span")
		if element.attrib.get("rend") is not None:
			span2.text = str(element.attrib.get("rend"))+" "
		else:
			span2.text = " "
		span2.attrib["class"] = "crit"
		element.insert(1, span2)
	return doc

# Add class based on rend
def rend_to_class(doc):
	for element in doc.iter("tei-hi"):
		element.attrib["class"] = element.attrib["rend"]
	return doc

# Add line numbers
def add_line_numbers(doc):
	for element in doc.iter("tei-l"):
		m = re.match(ur'(.+\..+\.)([0-9]+)', element.attrib["xml:id"])
		if int(m.group(2)) % 5 == 0:
			element.attrib["data-lineno"] = m.group(2)
	return doc

# Move titles to after nearest pb -- This hack will fail if they are 
# not the pb does not immediate follow the head. Something using 
# itersiblings() probably needs to be added.
def move_titles(tree):
	for element in tree.xpath("//text/body/div1"):
		title = element[0]
		pb = element[1]
		if title.tag == "head":
			element[0] = pb
			element[1] = title
	return tree

# Set dip class for tei-add so that carets are not displayed in the critical view
def remove_carets(tree):
	for element in tree.iter("add"):
		if element.text == u'\u2227':
			element.attrib["class"] = "dip"
	return tree

# Wrap special characters in diplomatic and critical span tags
def convert_special_characters(str):
	 # &#182; = pilcrow, &#8743; = caret
	p = ['&#42843;','&#383;', '&#182;']
	r = ['r', 's', '&#182; ',]
	for k,v in enumerate(p):
		str = str.replace(v, '<span class="dip">'+v+'</span><span class="crit">'+r[k]+'</span>')
	return str

# Wrap foreign strings
def wrap_foreign(str):
	return str.replace('xml:lang', 'class="foreign" xml:lang')
	#return re.sub(ur'xml:lang', 'class="foreign" xml:lang', str)

# Build html_pages
def build_html_pages(tree):
	move_titles(tree)
	remove_carets(tree)

	xml = etree.tostring(tree)

	# Build the pagination dictionary for future use
	pagination = {}
	i = 1
	for k, v in enumerate(re.findall('(<pb .+?\/>)', xml)):
		n = re.search(r'n=\"(.+?)\"', v)
		facs = re.search(r'facs=\"(.+?)\"', v)
		pagination[i] = [n.group(1), facs.group(1)]
		i = i+1

	# Insert AEMEMILESTONE delimiter
	xml = re.sub('(<pb )(.+?)(\/>)', lambda pat: 'AEMEMILESTONE'+pat.group(1)+pat.group(2)+pat.group(3), xml)
	xml = re.sub('\s+', ' ', xml)

	# Get a list of div1 elements
	p = re.compile("<div1.*?>.+?</div1>")
	div1s = re.findall(p, xml)
	# for x in div1s:
	# 	print(x[0:200])

	# Get a list of div1 tags (with attributes)
	div1Tags = re.findall("<div1.*?>", xml)
	# for x in div1Tags:
	# 	print(x[0:200])

	pages = []
	pbs = xml.split('AEMEMILESTONE')
	# Wrap the list items in <pb>...</pb>
	for i, item in enumerate(pbs):
		  item = item + '</div1></pb>'
		  # Remove duplicate </div1> tags
		  item = item.replace('</div1></div1>', '</div1>')
		  pbs[i] = item
	# Get the <div1> string from the first item by removing </pb>
	startTag = pbs[0].replace('</pb>', '')
	# Insert the <div1> start tag after each <pb>
	for i, item in enumerate(pbs):
		pbs[i] = re.sub('(<pb .?>)', lambda pat: pat.group(1)+startTag, pbs[i])
	# Remove the redundant first item
	del pbs[0]
	pages.append(pbs)

	''' This is the old algorithm that ends the page at every text boundary. '''
	# # Get a list of lists containing each page wrapped in pb and div1 tags (with attributes)
	# pages = []
	# for i, div1 in enumerate(div1s):
	# 	# Get a list of all strings starting with a pb tag
	# 	pbs = div1.split('AEMEMILESTONE')
	# 	# print(pbs)
	#  	# Strip div1 tags and wrap the pbs strings in div1 (with attributes) and '</pb></div1>'
	#  	for k, v in enumerate(pbs):
	#  		pbs[k] = div1Tags[i]+ re.sub("<?\/div1>|<div1.*?>", "", v) +"</pb></div1>"
	# 	# print(pbs)
	#  	# Remove any empty elements
	#  	pbs = filter(None, pbs)
	#  	# Delete the first element
	#  	del pbs[0]
	#  	# Append to the list of lists
	#  	pages.append(pbs)

	# Flatten the list of lists into a list of each page
	pages = [x for x in pages[0]]

	# Convert each page into well-formed html
	html_pages = []
	for page in pages:
		# Handle the head tag temporarily by adding extra tei- prefix
		page = re.sub('<head rend=\"critical\">(.+)</head>', lambda pat: '<tei-head rend="critical">' + pat.group(1) + '</tei-head>', page)
		doc = html.fromstring(page)

		# Add the tei- prefix to all elements
		for element in doc.iter(tag=etree.Element):
			element.tag = "tei-"+element.tag

		doc = rend_to_class(doc)
		doc = add_line_numbers(doc)
		doc = reformat_notes(doc)
		doc = replace_pointing(doc)

		result = etree.tostring(doc, pretty_print=True, method="html")
		# Remove the extra tei- prefix on head elements
		result = result.replace('tei-tei-', 'tei-')
		# result = wrap_ln_caps(result) # Causes error
		result = wrap_foreign(result)
		html_pages.append(convert_special_characters(result))

	# print(len(html_pages)) # Needs to be trimmed of "\n"
	# html_pages = ['this', 'that']

	return html_pages, pagination

@app.route('/viewer', methods=["GET", "POST"])
def viewer():
	menu = buildMenu()

	# Build file path based on GET/POST
	APP_STATIC = os.path.join(app.root_path, 'static')
	file = 'content/xml/'
	if request.method == "POST":
		file = file + request.json[0]["url"]
	else:
		file = file + 'cover.xml'#'bodllaudmisc108/3aa_SEL-Brendan.xml'		
	filepath = os.path.join(APP_STATIC, file)	

	# Get the xml for edit mode
	with open(filepath, "r") as fn:
		xmlstr = fn.read().decode('utf-8')

	# Read xml file as string and parse it as xml
	tree = strip_ns(etree.parse(filepath))
	#tileSource = build_tileSource(tree)

	# Build the html_pages and pagination objects, then dump the pages to a temp file
	html_pages, pagination = build_html_pages(tree)
	pageList = json.dumps(html_pages)
	filepath = os.path.join(APP_STATIC, "content/xml/tmp.txt")
	with open(filepath, "w") as fn:
		fn.write(pageList)

	# Hack: replace the rendered text on the splash page
	if request.method != "POST":
		html_pages = ['<h1 class="splash">'+app.config["SPLASH"]+'</h1>']

	# Render the template
	return render_template('edition_viewer.html', MENU=menu, text=html_pages, pagination=pagination, filepath=filepath, xmlstr=xmlstr)

@app.route('/viewer/load-text', methods=["GET", "POST"])
def loadText():
	# Build file path based on GET/POST
	#APP_STATIC = os.path.join(app.root_path, 'static')
	APP_STATIC = "static"
	file = 'content/xml/' + request.json[0]["title"]
	newfilepath = os.path.join(APP_STATIC, file)

	# Get the xml for edit mode
	with open(newfilepath, "r") as fn:
		xmlstr = fn.read().decode('utf-8')

	# Read xml file as string and parse it as xml
	tree = strip_ns(etree.parse(newfilepath))

	# Build the html_pages and pagination objects, then dump the pages to a temp file
	html_pages, pagination = build_html_pages(tree)
	pageList = json.dumps(html_pages)
	filepath = os.path.join(APP_STATIC, "content/xml/tmp.txt")
	with open(filepath, "w") as fn:
		fn.write(pageList)

	# print(pagination)
	# Return the new text data to the template
	data = json.dumps({"html_pages": html_pages[0], "pagination": pagination, "filepath": newfilepath, "xmlstr": xmlstr})
	return data

@app.route('/viewer/load-page', methods=["GET", "POST"])
def loadPage():
	# Get the pageIndex from the current page by POST
	pageIndex = int(request.json[0]["page"])-1

	# Read the temp file
	APP_STATIC = os.path.join(app.root_path, 'static')
	filepath = os.path.join(APP_STATIC, "content/xml/tmp.txt")
	with open(filepath, "r") as fn:
		pages = json.loads(fn.read())

	# Return the appropriate page to the template
	data = json.dumps({"html_pages": pages[pageIndex+1]})
	return data

@app.route('/viewer/get-source', methods=["GET", "POST"])
def getSource():
	# Build file path based on GET/POST
	APP_STATIC = os.path.join(app.root_path, 'static')
	file = 'content/xml/'
	url = request.json[0]["url"]
	if request.method == "POST":
		file = file + url
	else:
		file = file + 'cover.xml'#'bodllaudmisc108/3aa_SEL-Brendan.xml'		
	filepath = os.path.join(APP_STATIC, file)
	print(filepath)	

	# Read xml file as string and parse it as xml
	parser = etree.XMLParser(ns_clean=True, resolve_entities=False)
	tree = etree.parse(filepath, parser)
	# Convert it to a string
	source = etree.tostring(tree, pretty_print=False, method="xml", encoding="UTF-8")
	source = re.sub('&(.+);', lambda pat: '&amp;'+pat.group(1)+';', source)
	return source

@app.route('/viewer/save-xml', methods=["GET", "POST"])
def saveXML():
	filepath = request.headers["filepath"]
	xmlstr = request.get_data()
	result = validate(xmlstr)
	if result == "valid" and app.config["DEMOMODE"] == False:
		# Write the file
		print("Saving")
		file = open(filepath, "w")
		file.write(xmlstr)
		file.close()
		result = 'success'
	else:
		result = '<p>The editor is in demo mode. Changes cannot be saved.</p>'
	return result

def validate(xml):
    """
    Args:
        `xml` takes a path to an xml file, assumed to be in TEI
        `schema` takes a path to an rng file
    Returns:
        `True` is valid; otherwise, `False`
	"""
    from io import BytesIO
    from lxml import etree

    # Read the schema into a file-like object
    schema_file = 'static/lib/validation/oxgarage.rng'
    with open(schema_file, 'r') as f:
        schema = BytesIO(f.read())

    # Construct the validator
    schema_xml = etree.parse(schema) # Parse the schema as XML -- assumed to be valid
    validator = etree.RelaxNG(schema_xml)  # Convert the XML to an relaxng validator

    # Read the TEI file into a file-like object
    tei = BytesIO(xml)
    
    # Parse the TEI file as XML
    errors = ""
    try:
        doc = etree.parse(tei)
        # If the document does not validate, build the error message
        if not validator.validate(doc):
            for error in validator.error_log:
                errors+= "ERROR ON LINE %s: %s.<br>" % (error.line, error.message.encode("utf-8"))
    # The XML is not well formed or cannot be parsed
    except etree.XMLSyntaxError, e:
        # Build the error message
        for error in e.error_log:
            errors+= "ERROR ON LINE %s: %s.<br>" % (error.line, error.message.encode("utf-8"))
        pass

    # If there are no errors, return valid; otherwise return the errors
    if errors == "":
        return "valid"
    else:
        return "<p>The document is not valid. Here are the errors from the log:</p>" + errors

@app.route("/")
def index():
	menu = buildMenu()
	return render_template('home.html')

@app.route("/about")
def about():
	menu = buildMenu()
	return render_template('about.html')

@app.route("/downloads")
def downloads():
	return render_template('downloads.html')

@app.route("/credits")
def credits():
	return render_template('credits.html')

@app.route("/metadata")
def metadata():
	"""
	Builds an HTML template of the metadata which can be passed 
	to the Flask view.
	"""
	APP_STATIC = os.path.join(app.root_path, 'static')
	file = 'content/xml/sampleteiHeader.xml'
	filepath = os.path.join(APP_STATIC, file)	
	metadata = managers.metadata.getMetadata(filepath)
	template = managers.metadata.buildTemplate(metadata)
	return render_template('metadata.html', metadata=template)

@app.route("/view/get-metadata", methods=["GET", "POST"])
def getmetadata():
	"""
	Ajax version of metadata(). Builds an HTML template of the metadata which can be passed to an Ajax response.
	"""
	APP_STATIC = os.path.join(app.root_path, 'static')
	file = 'content/xml/'+ request.json[0]["file"]
	filepath = os.path.join(APP_STATIC, file)	
	metadata = managers.metadata.getMetadata(filepath)
	template = managers.metadata.buildTemplate(metadata)
	return json.dumps(template)

@app.route("/guidelines", methods=["GET", "POST"])
def guidelines():
	menu = buildMenu()
	# Search function has been used -- display results
	if request.args:
		query = request.args.get('q')
		search_results = True
	else:
		search_results = False
	return render_template('guidelines.html', search_results=search_results)

@app.route("/get-markdown", methods=["GET", "POST"])
def getMarkdown():
	file = "static/guidelines/" + request.get_data() + ".md"
	# l = request.get_data().split("/")
	# title = l[-1]
	# title = re.sub('[0-9]+_', "# ", title)
	# title = title.replace("xml_id", "`xml:id`")
	# title = title.replace("_", " ")
	# print(title)
	import markdown, codecs
	input_file = codecs.open(file, mode="r", encoding="utf-8")
	text = input_file.read()
	# text = title + "\n\n" + text
	html = markdown.markdown(text, extensions=['markdown.extensions.extra', 'markdown.extensions.admonition'])
	return html


@app.template_filter() # Register template filter
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)
app.jinja_env.filters['regex_replace'] = regex_replace

''' 
@app.route("/")
def hello():
    return "Flask works! Now onto the development phase! Renaming app...\n"
'''

app.config['DEBUG'] = True
if __name__ == "__main__":
    app.run()