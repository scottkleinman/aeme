The `<msIdentifier>` contains information required to identify the manuscript being described.

### AEME Requirements

AEME requires that <msIdentifier> have the following child elements:

* `<settlement>`: The city in which the manuscript is currently located.
* `<repository>`: The repository in which the manuscript is located.
* `<collection>`: The collection or fond within the repository in which the manuscript is located. This element is optional if the full library shelfmark does not contain a collection identifier.
* `<idno>`: The standard number used to identify the manuscript (e.g. shelfmark).

For example:

```xml
<msIdentifier>
<settlement>Oxford</settlement>
<repository>Bodleian Library</repository>
<collection>Laud Misc.</collection>
<idno>108</idno>
</msIdentifier>
```

Abbreviations (e.g. “Bodleian” or "BL”) should be avoided, except in `<collection>`, where they are traditional. In this case, abbreviated words should be indicated by a full stop (i.e. “Misc.” instead of “Misc”). The abbreviation “MS” should be excluded, but must be present in the `<title>` element of the `<titleStmt>` if it is part of the common identifier for the manuscript.

AEME will employ short names in place of sigla. Short names should be based on the `<msIdentifier>` content, which will generally follow the filenames created from the same content, but without the xml extension.

Where the manuscript had a previous identifier, it may optionally be included using `<altIdentifier type="former">`.
