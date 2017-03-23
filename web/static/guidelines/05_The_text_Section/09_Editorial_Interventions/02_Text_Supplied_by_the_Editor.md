# Text Supplied by the Editor

The `<supplied>` element may be used where text is missing or completely illegible at the editor’s discretion. It should be used in combination with `<damage>` or `<unclear>` tags to indicate the causative agent for the loss of text, where determinable.

Supplied text can be based on reference to another source or by conjecture, but note that it is not AEME policy to supply alternative readings from other witnesses to the text.

For editorially supplied word divisions, see the section on [Word Division](02_Encoding_Policies/02_Word-Level_Representations/01_Word_Division).

Standard attributes for `<supplied>` are as follows:

* `@reason`: Indicates why the material had to be supplied. Standard values for this attribute are “torn”, “faded”, “rubbed”, “smeared”, “overbound”, “stained”, and “patched”. 
* `@resp`: Indicates the editor responsible for supplying the letter, word, or passage contained within the `<supplied>` element. The default is the initials of the named editor(s) as they appear in the `<teiHeader>`, and need not be recorded.
* `@source`: States the source of the supplied text (the editor’s initials in the case of conjecture). N.B. This is valid P5, but we should probably use `@resp` to indicate editorial responsibility and `<ref>` if the supplied text comes from an external source.
* `@hand`: Indicates the scribal hand responsible for the damage that obliterated the text, where determinable.
