""" Python variables must be all upper case and temporary variables
all lower case. This ensures the creation of readable dictionaries in 
this file without duplicating material in the JSON object passed to 
the template.
"""

SITE_TITLE = "The Archive of Early Middle English"

SPLASH = "Select a Text from the Menu"

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
