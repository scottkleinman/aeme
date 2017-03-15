## File Naming and Organisation

Since AEME edits at the codex level, it makes sense to assemble one file per codex (or equivalent). It is possible to have multiple interim/working files for individual texts. Filenames will be composed from the information in the `<collection>` and `<idno>` elements of the `<msDesc>` element. Information in `<collection>` should be converted to lower case and may be abbreviated.

If there is no `<collection>` information, the material in `<repository>` should be used with the same abbreviation rules. For example: “bodllaudmisc108.xml” for Oxford, Bodleian Library, Laud Misc. MS 108; “salisc82.xml” for Salisbury Cathedral, MS 82. Note that multi-college institutions like Oxford and Cambridge should contain prefixes like “ox” and “cam” before the college names. Some manuscripts contain punctuation marks in their shelf ID numbers. These should be changed to underscores. If there are multiple files, the suffix -01, -02, etc. can be added before the xml extension.

AEME maintains a working table of equivalents for abbreviations and full `<collection>` values. Image files will be formed from the equivalent transcription filename (minus the xml extension) combined and the image filename delivered by the holding repository. The transcription filename and the image filename will be divided by _img_. For example, laudmisc108_img_0001.tif, salisc82_img_salisc0082.tif.

Note that this may provide a little bit of redundancy, but it ensures that the filename, which may be meaningless, is always accompanied by information about the manuscript from which the image is taken.

TEI and image files will be maintained in separate directories.

## `xml:id` Values

TEI’s `@xml:id` is used to create a canonical reference to be used for processing. Since it is not seen by the reader on the front end, its value may be entirely arbitrary, but AEME recommends assigning values that are at least somewhat human readable. This serves as a finding aid and is helpful for anyone re-using the code in the future. The value of an `@xml:id` attribute should be unique within a file. However, it is frequently useful for named entities to have unique values used consistently across the Archive. AEME maintains a named entity file for this purpose. At present, AEME has not fully developed conventions for `@xml:id` values to be used universally. So far, values for persons are prefixed with `bio`, values for places with `loc`, and values for organisations with `org`. For example, `bioGO001` refers to Sharon Goetz (using the first two letters of her surname). These conventions may become more rigorous as content increases in the Archive.

For bibliographical references, the `@xml:id` should be formed from the surname of the author and the date of publication. Ambiguous names can use the author’s initial (e.g. HorstmannC1873). Multiple publications from the same year can be indicated with a suffixed number (e.g. Horstmann1873-1). Other identifiers (e.g. based on ISBNs or DOIs) may be used of the author-date conventions are not appropriate. The only requirement is that Bibliographical `@xml:id` values must be unique within the file, but, in practice, it should also be unique across the Archive, drawn from a stand-off document. These may be accessed using `@corresp` in a `<ref>` or `<bibl>` element.

Standard TEI P5 practice is to indicate languages by attaching `@xml:lang` to appropriate elements (e.g. `<seg xml:lang="enm">`). AEME follows MESA in requiring the use of language codes from the ISO 639-2 Language Code List. The value of `@xml:lang` must be from the first column (ISO 639-2 Code).

## AEME Bibliographic Style

Bibliographic references should be given in Chicago Manual of Style, 16th edition format if they are unstructured (e.g. complete references in a `<p>` element). Structured bibliographic references should generally contain all the same information. Titles should enclosed in `<title>` tags where they would normally be rendered in italics in a print publication.

## Editorial Abbreviations and Sigils

“Folio” and “folios” will be abbreviated “f.” and “ff.” instead of “fol.” and “fols.” In editorial notes, sigils should be listed by the base text sigil first, followed by the beta and alpha sigils in an order designated by AEME for texts with multiple witnesses.

## Names of Saints

Saints’ names can often go by multiple spellings. For consistency, AEME uses spellings from David Hugh Farmer, David Hugh. _The Oxford Dictionary of Saints_. 5th edition Oxford: Oxford University Press, 2003. If the saint is not listed in Farmer, a secondary reference is Cross, F. L., and E. A. Livingstone. _The Oxford Dictionary of the Christian Church_. 3rd Revised edition. Oxford; New York: Oxford University Press, 2005. Each saint should receive a unique `@xml:id` in AEME’s list of named entities, and editors should adopt a consistent spelling in notes and discussion. However, editors should be aware that in some cases English spellings of names, such as for Welsh or Irish saints, may have political implications and are urged to account for these factors.

## Metadata

The primary encoding of metadata will be placed within the `<teiHeader>` sections of the document TEI file. AEME requires the minimum set of metadata elements specified in this document. AEME also maintains directories containing metadata files for easy interoperability with resources such as TAPAS, MESA, and Manuscripts Online. At the time of writing, AEME expects to maintain RDF files for MESA and the Dublin Core files generated by TAPAS. Other metadata options may be added at a later date.

## Document File Structure

Each document object is contained within a single TEI file (although the file may reference outside content). The discussion below describes a TEI P5-compliant template that must be used as the basis for each document object file.

Files must begin with an appropriate XML declaration and an AEME namespace declaration. If character entity aliases are used, they must be defined using DTD subsets. For example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE TEI[
<!ENTITY yogh "&#x021D;">
]>
<TEI xml:id="$TBD" xmlns="http://www.tei-c.org/ns/1.0" xmlns:aeme="http://aeme.emesoc.org/ns/1.0" xsi:schemaLocation="http://aeme.emesoc.org/schema/aeme.rng">
...
</TEI>
```

Line 1 declares the document to be xml and the character encoding to be UTF-8 (Unicode). Lines 2-4 declare an alias for the Unicode code point for yogh: `&#x021D;` using a DTD subset. This ensures that instances of `&yogh;` in the file will be replaced by the Unicode character for yogh in any output. See the section on Representation of Individual Characters and Glyphs for further details.

Line 5 begins the TEI document, declaring the TEI namespace as well as the AEME namespace. This will serve to disambiguate any overlap between standard TEI and custom AEME uses. The content of the TEI document is contained between lines 5 and 7.

Note: We are not currently using the AEME namespace, so `@xmlns:aeme` may be omitted. The use of `@xml:id` in the `<TEI>` tag is a useful hook for output processing. The value should match the filename minus the `.xml` extension, e.g. `bodllaudmisc108`.

The primary encoding of metadata will be placed within the `<teiHeader>` ection at the top of the `<TEI>` element. Standard single-text files will be composed of a `<teiHeader>` element, a `<facsimile>` element, and a `<text>` element. Elements containing glossaries or other editorial apparatus may be produced in separate files during the draft stage but should be placed in a single file prior to publication.