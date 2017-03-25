import os, re, datetime
from bs4 import BeautifulSoup, Comment 

def stripComments(soup):
	"""
	Strips comments from the parsed soup object.
	"""
	comments = soup.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]
	return soup

def bsTag2str(tag):
	"""
	Converts a Beautiful Soup Tag to a Unicode string but 
	preserves internal tags. Also removes extra white space.
	"""
	tag_str = ""
	for x in tag.contents:
		tag_str += unicode(x) + " ".strip()
	tag_str = re.sub("\s+", " ", tag_str)
	return tag_str

def ref2Link(ref):
	"""
	Convert ref elements to HTML links
	"""
	for ref in soup.find_all('ref'):
		if ref.attrs:
			for k, v in ref.attrs.items():
				if k == "target":
					link = soup.new_tag("a")
					link['href'] = v
					if v[0] is not "#":
						link['target'] = '_blank'
					link.string = ref.get_text()
					ref.replace_with(link)

def getTitles(teiHeader):
	"""
	Retrieves the titleStmt titles(s). Returns a dict
	with the main title and a list of alternative titles.
	"""
	altTitles = []
	titleStmt = teiHeader.fileDesc.titleStmt
	if titleStmt.title.title:
		titles = titleStmt.title.find_all('title')
		for title in titles:
			if title["type"] == "main":
				mainTitle = title.string.strip()
			else:
				altTitles.append(title.string.strip())
	else:
		mainTitle = titleStmt.title.string
	titles = {"main": mainTitle, "alt": altTitles}
	return titles

def getResponsibility(teiHeader):
	"""
	Retrieves the respStmt element(s). Returns a dict
	with the main title and a list of alternative titles.
	"""
	responsibility = []
	if teiHeader.fileDesc.titleStmt.respStmt:
		statements = teiHeader.fileDesc.titleStmt.find_all('respStmt')
		# For each respStmt, create a dict with the resp element
		# and a list of name elements
		for statement in statements:
			stmt = {"resp": statement.resp.string, "names": []}
			for name in statement.resp.next_siblings:
				stmt["names"].append(name.string.strip())
			# Filter empty elements	
			stmt["names"] = filter(bool, stmt["names"])
			responsibility.append(stmt)
	# A list of respStmt dicts
	result = []
	# Turn the list of names into a comma-separated strings
	for item in responsibility:
		names = item["names"]
		if len(names) > 1:
			names.insert(-1, "and")
		names = ", ".join(names)
		names = names.replace(", and, ", ", and ")
		result.append(item["resp"] + " " + names + ".")
	return result

def getPublicationDate(teiHeader):
	"""
	Returns the publication date or "Unknown".
	"""
	if teiHeader.fileDesc.publicationStmt.date:
		return teiHeader.fileDesc.publicationStmt.date.string
	else:
		return "Unknown"

def getRevisions(teiHeader):
	"""
	Returns a list of revisionDesc changes as a string with 
	@when and @who incorporated.
	"""
	revisions = []
	for change in teiHeader.revisionDesc.find_all('change'):
		when = datetime.datetime.strptime(change["when"], "%Y-%m-%d").strftime("%d %B, %Y")
		who = change["who"]
		text = change.string.strip()
		revisions.append(when + ": " + text + " By " + who + ".")
	return revisions

def makeHtmlTitle(title, title_str, soup):
	# Scrub white space from the element
	new_title = re.sub("\s+", " ", title_str).strip()
	# Add an em tag to the soup
	em = soup.new_tag("em")
	# Give the em tag a class
	em['class'] = 'title'
	# Assign the title string to the em tag
	em.string = new_title
	# Replace the original title tag
	title.replace_with(em)

def getMSContents(teiHeader, soup):
	"""
	Returns a dict of msContents, containing a summary element, if 
	present, and a list of msItems. Each msItem has a locus and title  
	elements, as well as a list of bibl elements. Titles within 
	bibl elements are wrapped in HTML em tags.
	"""
	contents = {"summary": "", "msItems": ""}
	# Fetch summary
	summary = teiHeader.fileDesc.sourceDesc.msDesc.msContents.summary
	if summary:
		summary_str = bsTag2str(summary)
		contents["summary"] = summary_str
	msItems = []
	# Fetch each msItem
	for item in teiHeader.fileDesc.sourceDesc.msDesc.msContents.find_all("msItem"):
		# Iterate through the bibl elements in the listBibl
		listBibl = item.listBibl.find_all("bibl")
		bibliography = []
		for bibl in listBibl:
			if bibl.title:
				makeHtmlTitle(bibl.title, bibl.title.string, soup) 
				bibl_str = bsTag2str(bibl)
			else:
				bibl_str = bibl.get_text()
			bibliography.append(bibl_str)         
		msItems.append({
				"locus": item.locus.get_text(),
				"title": item.title.get_text(),
				"bibliography": bibliography
			})
		contents["msItems"] = msItems
	return contents

def getPhysDesc(teiHeader):
	"""
	Returns a dict with lists of handNotes, scriptNotes, and 
	decoNotes, if present.
	"""
	notes = {"handnotes": [], "scriptnotes": [], "deconotes": []}
	physDesc = teiHeader.fileDesc.sourceDesc.physDesc
	if physDesc.handDesc:
		for note in physDesc.handDesc.find_all("handNote"):
			note_str = bsTag2str(note)
			notes["handnotes"].append(note_str)
	if physDesc.scriptDesc:
		for note in physDesc.scriptDesc.find_all("scriptNote"):
			note_str = bsTag2str(note)
			notes["scriptnotes"].append(note_str)
	if physDesc.decoDesc:
		for note in physDesc.decoDesc.find_all("decoNote"):
			note_str = bsTag2str(note)
			notes["deconotes"].append(note_str)
	return notes

def getHistory(teiHeader):
	"""
	Returns a dict with the items in the history element, if any: origin, provenance, and acquisition.
	"""
	history = {}
	sourceDesc = teiHeader.fileDesc.sourceDesc
	if sourceDesc.history.origin:
		origin = re.sub("\s+", " ", unicode(sourceDesc.history.origin))
		history["origin"] = origin.strip()
	if sourceDesc.history.provenance:
		provenance = re.sub("\s+", " ", unicode(sourceDesc.history.provenance))
		history["provenance"] = provenance.strip()
	if sourceDesc.history.acquisition:
		acquisition = re.sub("\s+", " ", unicode(sourceDesc.history.acquisition))
		history["acquisition"] = acquisition.strip()
	return history

# Open the source file, remove comments, and get the teiHeader
def getMetadata(filepath):
	with open(filepath) as f:
		soup = BeautifulSoup(f, 'xml')
	soup = stripComments(soup)
	# soup = ref2Link(soup)
	# Only gets the first level
	for ref in soup.find_all('ref'):
		if ref.attrs:
			for k, v in ref.attrs.items():
				if k == "target":
					link = soup.new_tag("a")
					link['href'] = v
					if v[0] is not "#":
						link['target'] = '_blank'
					link.string = ref.get_text()
					ref.replace_with(link)

	teiHeader = soup.teiHeader
	metadata = {} 

	# Retrieve the metadata and store it in variables
	metadata["titles"] = getTitles(teiHeader)
	metadata["publicationDate"] = getPublicationDate(teiHeader)
	metadata["responsibility"] = getResponsibility(teiHeader)
	metadata["revisions"] = getRevisions(teiHeader)
	metadata["contents"] = getMSContents(teiHeader, soup)
	metadata["physDesc"] = getPhysDesc(teiHeader)
	metadata["history"] = getHistory(teiHeader)

	return metadata

def buildTemplate(metadata):
	## Template variables
	# Main title
	maintitle = metadata["titles"]["main"]
	# HTML list of any alterntive titles
	if len(metadata["titles"]["alt"]) > 0:
		altTitles = "<ul>"
		for item in metadata["titles"]["alt"]:
			altTitles += "<li>"+item+"</li>"
		altTitles += "</ul>"
	# Publisher and Publication date
	publicationDate = metadata["publicationDate"]

	## Build Template
	template = ""
	template += "<h1>"+maintitle+"</h1>"
	if len(metadata["titles"]["alt"]) > 0:
		template += "<p>Also known as:</p>"+altTitles
	template += "<p>Published by The Archive of Early Middle English, "+publicationDate+".</p>"
	# Responsibility
	for item in metadata["responsibility"]:
		template += "<p>"+item+"</p>"
	# Revisions
	if len(metadata["revisions"]) > 0:
		template += "<p><strong>Revision History:</strong></p>"
		template += "<ul>"
		for item in metadata["revisions"]:
			template += "<li>"+item+"</p>"
		template += "</ul>"
	# Contents
	template += "<h3>Contents</h3>"
	if metadata["contents"]["summary"]:
		template += "<p><strong>Summary:</strong> "+metadata["contents"]["summary"]+"</p>"
	for item in metadata["contents"]["msItems"]:
		template += "<p>"+item["locus"]+": "+item["title"]+"<br>"
		if len(item["bibliography"]) > 0:
			template += "<strong>Bibliography:</strong><br>"
			template += "<ul>"
			for bibl in item["bibliography"]:
				# Wrap urls and # targets in html links
				bibl = bibl.strip()
				if bibl[0:5] == "http:":
					bibl = '<a href="'+bibl+'" target="_blank">'+bibl+'</a>'
				if bibl[0] == "#":
					bibl = '<a href="'+bibl+'">'+bibl+'</a>'
				template += "<li>"+bibl+"</li>"
			template += "</ul></p>"
	# Physical Description
	if metadata["physDesc"]:
		template += "<h3>Physical Description</h3>"
		if metadata["physDesc"]["handnotes"]:
			template += "<h4>Hand Notes</h4>"
			template += "<ul>"
			for note in metadata["physDesc"]["handnotes"]:
				template += "<li>"+unicode(note)+"</li>"
			template += "</ul>"
		if metadata["physDesc"]["scriptnotes"]:
			template += "<h4>Script Notes</h4>"
			template += "<ul>"
			for note in metadata["physDesc"]["scriptnotes"]:
				template += "<li>"+unicode(note)+"</li>"
			template += "</ul>"
		if metadata["physDesc"]["deconotes"]:
			template += "<h4>Decoration Notes</h4>"
			template += "<ul>"
			for note in metadata["physDesc"]["deconotes"]:
				template += "<li>"+unicode(note)+"</li>"
			template += "</ul>"
	# History
	if metadata["history"]:
		template += "<h3>Manuscript History</h3>"
		if metadata["history"]["origin"]:
			template += "<h4>Origin</h4>"
			template += "<p>"+metadata["history"]["origin"]+"</p>"
		if metadata["history"]["provenance"]:
			template += "<h4>Provenance</h4>"
			template += "<p>"+metadata["history"]["provenance"]+"</p>"
		if metadata["history"]["acquisition"]:
			template += "<h4>Acquisition</h4>"
			template += "<p>"+metadata["history"]["acquisition"]+"</p>"

	return template