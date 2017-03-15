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

Line 1 declares the document to be xml and the character encoding to be UTF-8 (Unicode). Lines 2-4 declare an alias for the Unicode code point for yogh: `&#x021D;` using a DTD subset. This ensures that instances of `&yogh;` in the file will be replaced by the Unicode character for yogh in any output. See the section on [Representation of Individual Characters and Glyphs](../Encoding_Policies/Representation_of_Characters_and_Glyphs) for further details.

Line 5 begins the TEI document, declaring the TEI namespace as well as the AEME namespace. This will serve to disambiguate any overlap between standard TEI and custom AEME uses. The content of the TEI document is contained between lines 5 and 7.

Note: We are not currently using the AEME namespace, so `@xmlns:aeme` may be omitted.
The use of `@xml:id` in the `<TEI>` tag is a useful hook for output processing. The value should match the filename minus the `.xml` extension, e.g. `bodllaudmisc108`.

The primary encoding of metadata will be placed within the `<teiHeader>` section at the top of the `<TEI>` element. Standard single-text files will be composed of a `<teiHeader>` element, a `<facsimile>` element, and a `<text>` element. Elements containing glossaries or other editorial apparatus may be produced in separate files during the draft stage but should be placed in a single file prior to publication.
