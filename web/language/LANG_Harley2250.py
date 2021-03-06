""" Python variables must be all upper case and temporary variables
all lower case. This ensures the creation of readable dictionaries in 
this file without duplicating material in the JSON object passed to 
the template.
"""
SITE_TITLE = "A Digital Edition of Harley 2250"

SPLASH = "Select a Text from the Menu"

# For dropdowns, include a list with the label as the first item
MENU_ITEMS = [
'<a id="about" href="#">About <span class="sr-only">(current)</span></a>',
'<a class="navLink" href="bodljunius1/junius1.xml">Junius 1</a>',
[
    'Laud Misc. 108',
    '<a class="navLink" href="harley2250/martin.xml">Saint Martin</a>',
    '<a class="navLink" href="harley2250/erkenwald.xml">Saint Erkenwald</a>'
    ]
]

about_msg = """
<p>This is a demonstration of the digital edition
platform for the Archive of Early Middle English. This version includes 
material from London, British Library, Harley 2250. This is an alpha
version used for development purposes. Any texts currently loaded are
incomplete fragments used to test functionality. Image loading time
will vary depending on your internet connection.</p><p>Clicking a word
will open a dialog and perform a simple search of the Middle English
Dictionary, adding a wildcard asterisk to the end of the word.
Obviously, this will not always produce the desired results, but
eventually words can be matched to MED IDs.</p>
"""
ABOUT = {"title": "Revenge of About This Site", "message": about_msg}