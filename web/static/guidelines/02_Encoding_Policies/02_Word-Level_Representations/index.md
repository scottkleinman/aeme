Non-standard ASCII characters are encoded in Unicode code points expressed as hexadecimal character entity references. For instance, the character þ is encoded as `&#x00FE;`. Wherever possible, Unicode hex references should be taken from those listed in the [MUFI 3.0 specs](http://www.mufi.info/specs/). 

Otherwise, editors should refer to the [Unicode charts](http://www.unicode.org/charts/). If possible, glyphs should be selected from those available in the Junicode font.

In order to enhance readability, it is possible to substitute aliases for numeric entities, but these should be declared as a DTD subset in the `<!DOCTYPE>` at the beginning of the file, as illustrated in the [Document File Structure](../Editing_Policies/Document_File_Structure) section above. Names of aliases should be taken from those listed in the [MUFI 3.0 specs](http://www.mufi.info/specs/) (e.g. `&thorn;` for `&#x00FE;`). AEME maintains a working list of common character entity names in `Character_Entities.xlsx`. During the draft stage, equivalents to numeric entities may be programmed in the oXygen code points template for easy access when transcribing in oXygen. However, upon completion, DTD subsets must be used for any entities not listed in `Character_Entities.xlsx`. However, although character entity aliases are conformant with TEI P5, some applications written for P5 do not support them. Therefore AEME recommends converting entities from aliases to numeric entities prior to publication. It is also possible to use Unicode characters that can be displayed in oXygen such as þ and ȝ during the draft stage. These too should be converted to entities prior to publication.

For glyphs not available in Unicode, AEME has added the gaiji module to its customisation of TEI. As a general rule, glyphs defined using this module should be reserved for facsimile markup. This is because AEME policy is to represent most glyphs with modern typographic equivalents in the diplomatic and critical views. Exceptions are discussed in the [Allographs](Representation_of_Characters_and_Glyphs/Allographs) section below.