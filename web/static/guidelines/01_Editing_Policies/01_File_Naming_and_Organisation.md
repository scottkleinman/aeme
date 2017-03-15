Since AEME edits at the codex level, it makes sense to assemble one file per codex (or equivalent). It is possible to have multiple interim/working files for individual texts.
Filenames will be composed from the information in the `<collection>` and `<idno>` elements of the `<msDesc>` element. Information in `<collection>` should be converted to lower case and may be abbreviated.

If there is no `<collection>` information, the material in `<repository>` should be used with the same abbreviation rules. For example: “bodllaudmisc108.xml” for Oxford, Bodleian Library, Laud Misc. MS 108; “salisc82.xml” for Salisbury Cathedral, MS 82. Note that multi-college institutions like Oxford and Cambridge should contain prefixes like “ox” and “cam” before the college names. Some manuscripts contain punctuation marks in their shelf ID numbers. These should be changed to underscores. If there are multiple files, the suffix `-01`, `-02`, etc. can be added before the xml extension.

AEME maintains a working table of equivalents for abbreviations and full `<collection>` values.
Image files will be formed from the equivalent transcription filename (minus the xml extension) combined and the image filename delivered by the holding repository. The transcription filename and the image filename will be divided by `_img_`. For example, `laudmisc108_img_0001.tif`, `salisc82_img_salisc0082.tif`.

Note that this may provide a little bit of redundancy, but it ensures that the filename, which may be meaningless, is always accompanied by information about the manuscript from which the image is taken.

TEI and image files will be maintained in separate directories.
