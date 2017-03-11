""" Python variables must be all upper case and temporary variables
all lower case. This ensures the creation of readable dictionaries in 
this file without duplicating material in the JSON object passed to 
the template.
"""
SITE_FOLDER = "/"

SITE_TITLE = "The Archive of Early Middle English"

SPLASH = "Select a Text from the Menu"

# For dropdowns, include a list with the label as the first item
MENU_ITEMS = [
'<a id="about" href="#">About <span class="sr-only">(current)</span></a>',
'<a class="navLink" href="bodljunius1/junius1.xml">Junius 1</a>',
[
    'Laud Misc. 108',
    '<a class="navLink" href="bodllaudmisc108/3aa_SEL-Brendan.xml">Saint Brendan</a>',
    '<a class="navLink" href="bodllaudmisc108/3ac_SEL-Julian.xml">Saint Julian</a>',
    '<a class="navLink" href="bodllaudmisc108/3ah_SEL-George.xml">Saint George</a>',
    '<a class="navLink" href="bodllaudmisc108/6_Debate-between-Body-and-Soul.xml">Debate between the Body and Soul</a>'
    ]
]

about_msg = """
<p>This is a demonstration of the digital edition
platform for the Archive of Early Middle English. This is an alpha
version used for development purposes. Any texts currently loaded are
incomplete fragments used to test functionality. Image loading time
will vary depending on your internet connection.</p><p>Clicking a word
will open a dialog and perform a simple search of the Middle English
Dictionary, adding a wildcard asterisk to the end of the word.
Obviously, this will not always produce the desired results, but
eventually words can be matched to MED IDs.</p>
"""
ABOUT = {"title": "Revenge of About This Site", "message": about_msg}
