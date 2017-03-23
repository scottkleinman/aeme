# Deletions

`<del>` serves to mark up phrase-level deletions, and `<delSpan/>` marks up larger blocks. The `<del>` tag is used for short sequences of text, single words, or phrases. `<delSpan/>` must be used for larger level deletions because `<del>` tags do not carry over structural boundaries like `</l>`. `<delSpan/>` has the same attributes as `<del>`, with the addition of the `@spanTo` attribute, which refers to the spot where the deletion ends. Instead of the expected closing tag, `<delSpan/>` tags are bounded by an `<anchor/>` tag placed at the end of the span of added text.The `<anchor/>` element must have a valid `@xml:id` and should additionally contain `@type="delSpan"`.

`<del>` tags should be used where a word or passage is deleted or marked for deletion by a scribe, annotator, or corrector. The content of these tags may be either the characters that were deleted, if they are legible either under white or ultraviolet light, or symbolic if they are not legible. Symbolic representations of deleted characters should be supplied as follows: one period (.) per character up to five characters when it is possible to determine or guess the number of characters deleted, ...?... for deletions of six to a dozen characters, and ...?...?... for deletions of one half-line or more. Where multiple characters have been underdotted in the manuscript, only one `<del>` element is needed, unless the dotting represents separate acts of deletion.

If the deleted text is unclear, `<unclear>` tags may be nested within `<del>` tags. `<unclear>` tags give the option of expressing your degree of confidence in the reading. If the deleted text can be easily read, or, at the opposite extreme, cannot be read at all, there is no need to insert `<unclear>` tags.

Note: The `<del>` tag will be followed by `<add>` tags where a scribe has deleted and then substituted text.

For standard attributes used with `<del>`, see the section under [Unclear or Illegible Characters](05_The_text_Section/06_Unclear_or_Illegible_Characters).
