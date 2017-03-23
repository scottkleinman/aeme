# Unclear or Illegible Characters

Uncertainty about a reading can be caused by scribal deletion of the text or damage to the manuscript. TEI contains a group of closely related elements that classify these types of changes. These include `<gap>`, `<del>`, `<damage>`, `<unclear>`, and `<supplied>`. Their use can be summarized as follows:

* `<gap>`: Indicates a point where material has been omitted in a transcription, whether for editorial reasons described in the TEI header or because the material is illegible.
* `<del>`: Contains a letter, word, or passage deleted, marked as deleted, or otherwise indicated as superfluous or spurious in the copy text by a scribe, annotator, or corrector.
* `<damage>`: Contains an area of damage to the text witness not caused by erasure.
* `<unclear>`: Contains a word, phrase, or passage that cannot be transcribed with certainty because it is illegible.
* `<supplied>`: Signifies text supplied by the transcriber or editor for any reason, typically because the original cannot be read due to physical damage or loss to the original.

Note that the editor may supply text at his or her discretion, but it is not AEME policy to supply readings from alternate witnesses. These can be viewed by comparing the two witnesses side by side.

AEME avoids the use of the TEI `<certainty>` element and instead indicates degrees of certainty by attaching `@cert` to the above elements.

The functions of the above elements overlap, and some of them can be nested. AEME editors are encouraged to read closely the TEI documentation on the use of these elements in combination. Its recommendations are important enough to summarize here.

* Where the text has been rendered completely illegible by deletion or damage and no text is supplied by the editor in place of what is lost: place an empty `<gap>` element at the point of deletion or damage. Use the `@reason` attribute to state the cause (damage, deletion, etc.) of the loss of text.
* Where the text has been rendered completely illegible by deletion or damage and text is supplied by the editor in place of what is lost: surround the text supplied at the point of deletion or damage with the `<supplied>` element. Use the `@reason` attribute to state the cause (damage, deletion, etc.) of the loss of text leading to the need to supply the text.
* Where the text has been rendered partly illegible by deletion or damage so that the text can be read but without perfect confidence: transcribe the text and surround it with the `<unclear>` element. Use the `@reason` attribute to state the cause (damage, deletion, etc.) of the uncertainty in transcription and the `@cert` attribute to indicate the confidence in the transcription.
* Where there is deletion or damage but at least some of the text can be read with perfect confidence: transcribe the text and surround it with the `<del>` element (for deletion) or the `<damage>` element (for damage). Use appropriate attribute values to indicate the cause and type of deletion or damage. Observe that the `@degree` attribute on the `<damage>` element permits the encoding to show that a letter, word, or phrase is not perfectly preserved, though it may be read with confidence.
* Where there is an area of deletion or damage and parts of the text within that area can be read with perfect confidence, other parts with less confidence, other parts not at all: in transcription, surround the whole area with the `<del>` element (for deletion; or the `<delSpan>` element where it crosses a structural boundary); or the `<damage>` element (for damage). Text within the damaged area that can be read with perfect confidence needs no further tagging. Text within the damaged area that cannot be read with perfect confidence may be surrounded with the `<unclear>` element. Places within the damaged area where the text has been rendered completely illegible and no text is supplied by the editor may be marked with the `<gap>` element. For each element, one may use appropriate attribute values to indicate the cause and type of deletion or damage and the certainty of the reading.

Each of the above elements may take a number of attributes. AEME has not yet developed its own taxonomy of values for these attributes. The following, derived mostly from the Piers Plowman Electronic Archive, are provided for reference.

### Attributes for `<gap>`:

* `@reason`: Gives the reason for the omission. Standard attribute values are “ill-formed”, “torn”, “faded”, “rubbed”, “smeared”, “overbound”, and “stained”.
* `@hand`: In the case of text omitted from the transcription because of deliberate deletion by an identifiable hand, indicates the hand that made the deletion, where determinable.
* `@agent`: In the case of text omitted because of damage, categorizes the cause of the damage, if it can be identified. Standard attribute values are “water”, “mildew”, and “smoke”.
* `@quantity`: The extent of missing text in terms of the quantity of units specified in `@unit`.
* `@unit`: The type of unit used to measure missing text (e.g. “letters” or “millimeters”).

### Attributes for `<del>`:
* `@rend`: Indicates how the deletion was made in the text. Standard attribute values are “subpunction”, “erasure”, “overwritten”, “linedThrough”, “bracketed”, “underlined”.
* `@resp`: Indicates the editor responsible for identifying the hand of the deletion. The default will be the initials of the named editor(s) as they appear in the `<teiHeader>`, and need not be recorded.
* `@hand`: Identifies the scribe responsible for the deletion. The default is the current scribal hand.

### Attributes for `<damage>`:
* `@type`: Describes the damage. Standard attribute values are “torn”, “cropped”, “faded”, “rubbed”, “smeared”, “stained”, “overbound”, and “creased”.
* `@agent`: Signifies the cause of the damage. Standard attribute values are “torn” and “mildew”.
* `@extent`: Indicates the size of the damaged area. We have thus far used the imprecise unit of the space required for a character in the scribal hand, although the area affected may be described in inches, millimeters, folios, or whatever makes sense.
* `@resp`: Refers to the transcriber who makes the decision about the existence, type, and extent of the damage. The default will be the initials of the named editor(s) as they appear in the <teiHeader> and need not be recorded.

### Attributes for `<unclear>`:
* `@reason`: Indicates why the material is hard to transcribe. Standard attribute values are “ill-formed”, “torn”, “faded”, “rubbed”, “smeared”, “overbound”, and “stained”.
* `@resp`: Indicates the editor responsible for the transcription of the unclear text. The default will be the `@xml:id` of the named editor(s) as they appear in the `<teiHeader>` and need not be recorded.
* `@cert`: Signifies the degree of certainty ascribed to the unclear text. Values are “high”, “medium”, and “low”.
* `@hand`: Indicates the hand responsible for action that created the difficulty in transcription, where determinable.
* `@agent`: Signifies the causative agent for the difficulty. Standard values include “water” and “mildew”.
* `@extent`: Indicates the number of characters that are ambiguous or illegible.

### Attributes for `<supplied>`:

See the section on [Text Supplied by the Editor](05_The_text_Section/09_Editorial_Interventions/02_Text_Supplied_by_the_Editor).

