# Introduction

This document is a reference for editors who are encoding texts for the Archive of Early Middle English (AEME). All files submitted to the Archive must conform to the minimal Guidelines in the document. Encoding not specified in the Guidelines is allowable but may not be visible in the rendered texts on the AEME web platform.

AEME texts are encoded in the XML markup schema of the Text Encoding Initiative (TEI), following the <a href="http://www.tei-c.org/Guidelines/P5/" target="_blank">TEI P5 Guidelines</a>. In general, AEME sticks closely to the usage in TEI’s base modules with a few customisations. This document will note where AEME places limits on the larger set of allowable TEI elements and attributes. Where vocabulary and constraints are drawn from TEI, this document provides minimal explanation, particularly for possible child elements and attributes of many TEI elements. Editors should click the links to relevant TEI elements in order to read the appropriate TEI documentation.

These Guidelines do not represent a full statement of AEME editorial policy but they attempt to place encoding practices specific to AEME within the context of the editorial policy of the project.

## Some History
The initial draft is based primarily on the guidelines of the <a href="http://ccl/rch/uky.edu/using-TEI" target="_blank">Carolingian Canon Law Project</a>, the <a href="http://www.menota.org/HB_index.xml" target="_blank">Medieval Nordic Text Archive (Menota)</a>, and the <a href="http://www3.iath.virginia.edu/seenet/piers/protocoltran.html" target="_blank">*Piers Plowman Electronic Archive*</a>. AEME is gradually removing material derived from these projects.

## The Document Model
In AEME, each manuscript is conceived as a document object (or “document”, for short). This is to be distinguished from the genre of written texts often classified as “documentary” (e.g. legal and administrative texts). An AEME document is a digital object representing a manuscript that can be viewed in several ways, or views, in the AEME platform. These may be summarized as follows:

* Image View: A digital photograph of the manuscript.
* Facsimile View: A TEI-encoded representation of the manuscript’s codicological features, layout, illustrations, and other non-textual elements.
* Diplomatic View: A close transcription of the text components of the manuscript with minimal editorial intervention.
* Critical View: A transcription of the text components of the manuscript with greater editorial intervention, including most critical notes and references.

Each AEME document file must contain code to enable the rendering of a facsimile view, a diplomatic view, and a critical view of the manuscript. Image view is not required since digital images may not be available. Other types of views such as glossaries and translations may also be included, but these are not strictly part of the document representation.

AEME documents are divided into pages, each representing one side of a manuscript leaf. In the AEME platform, users may examine different views of individual pages side by side or superimpose one over another.

## Some More History
AEME initially adopted Menota’s division among three types of transcriptions, to be kept distinct by separate XML namespaces. As time passed, it became clear that a faithful facsimile rendering of the manuscript page was a tall order, and that what was really needed was a mock-up of the non-textual elements of the page in case no image was available. At the same time, TEI P5 has proven mostly adequate to combine codicological features with diplomatic and critical markup. Hence it was no longer necessary to keep the encoding for diplomatic and critical representations of the text strictly separate. Layout remains a troublesome issue, and AEME is exploring image annotation models (e.g. <a href="http://iiif.io/" target="_blank">SharedCanvas</a>) as one means of recording this information.

**Note on terminology:** A legacy of earlier usage has been the loose use of the terms “representation” and “layer” (e.g. “the critical representation”, “the facsimile layer”). These terms should now be avoided. Instead, we should discuss the “views” listed above, referring to the content that will appear to the user on the front end of the AEME platform. The terms “markup” or “encoding” (e.g. “the critical markup”, “the facsimile encoding”) should be used to refer to the code from which this content is generated. Terms like this should refer to markup primarily, though not exclusively, to be used to generate the equivalent type of view.

A related issue is the distinction between “transcription” as an activity of recording textual content, as well as the record itself, and “edition” which is the object presented to the public. Both the diplomatic and critical views are “editions” or “edited transcriptions”, that is, texts containing editorial interventions described in our editorial policies and these Guidelines.

## Some Conventions Used in This Document
Examples in this documentation may contain notation like `$TBD`. The dollar sign indicates that the value is a placeholder that will be replaced by some real value from the project. XML elements are always given in angular brackets, and attributes are referenced with `@` prefixed to the attribute name.
