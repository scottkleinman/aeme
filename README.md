aeme
====

AEME Development Repo

This repository contains the development code for the Archive of Early Middle English project (AEME). All transcriptions are provisional and should not be quoted. For further information, please go to http://aeme.emesoc.org/.

The top-level directory contains the oXygen project file (currently aeme0.2.xpr). The other contents of the repository are described below with notes regarding their use:

## The transcription folder
This contains one file, aeme-proofing.xsl, which is used to generate an html version of encoded texts for proofreading. Instructions for using the file can be found [here](https://github.com/scottkleinman/aeme/wiki/Transforming-XML-Files).

## The validation folder
This folder contains the AEME schema files and associated oXygen code templates:

* aeme0.3.5.rng
* aeme0.3.5.xml
* aeme_doc0.3.3.html
* aeme-oxygen-code-templates

## bodllaudmisc108
This folder contains all the files for Oxford, Bodleian Library, Laud Misc. 108. For development purposes, the codex is broken into multiple files, one text per file, and elements used by all the texts are maintained in standoff files as follows:

* entities.dtd -- a DTD subset of common character entities used in encoding the manuscripts of the text, as well as includes for standoff files
* teiheader.xml -- the common <teiHeader> element used in all texts in the manuscript
* facsimile.xml -- the common <facsimile> element used in all texts in the manuscript

In order to produce valid documents, the xml files for each text must begin with the following code:

```xml
<?xml version="1.0" encoding="UTF-8"?><?oxygen RNGSchema="http://www.emesoc.org/schema/aeme.rng" type="xml"?>
<!DOCTYPE TEI SYSTEM "entities.dtd">
<TEI xml:id="laudmisc108" xmlns="http://www.tei-c.org/ns/1.0">
    <!-- Standoff <teiHeader> and <facsimile> files --> &teiHeader; &facsimile;
    <!-- End of Standoff <teiHeader> and <facsimile> files -->
	<text>
	...
```

This will include all three standoff documents listed above.

Changes to the <teiHeader> should be appropriately documented in <revisionDesc>. Although changes to all files will be recorded in git commits, editors should also describe changes to the texts in the xml comments at the top of each file immediately after the `<text>` element.

## junius1
This folder contains all the files for Oxford, Bodleian Library, Junius 1. Currently, it contains two different versions of the manuscript xml:

* junius1.xml
* orm-mec.xml

## old
This folder contains files previously housed in this repository.