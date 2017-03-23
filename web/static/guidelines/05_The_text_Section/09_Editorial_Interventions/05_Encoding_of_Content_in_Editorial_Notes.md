# Encoding in Content of Editorial Notes

In certain instances, constant of editorial notes must be rendered by separate styling instructions from those used for the text transcription. AEME requires the following practices to accommodate this need:

* Text meant to be rendered in bold, italics, or superscript should be encoded using the `<hi>` element and `@rend` with the values of `bold`, `italic`, and `superscript`, respectively. These values are not allowed in the text transcription.
* AEME requires that parentheses within the text of a note be encoded as `&#0028;` and `&#0029;` (or equivalent aliases) so that the stylesheet can transform `<expan>` tags without transforming parentheses in notes.
