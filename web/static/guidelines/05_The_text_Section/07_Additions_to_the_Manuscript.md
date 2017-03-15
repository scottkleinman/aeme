The `<add>` tag serves to mark up phrase-level additions, and `<addSpan/>` marks up larger blocks. These should be used only to encode text introduced into the text after the initial writing (whether by the original scribe, contemporary, or later scribes), and never for editorially supplied text. For modern editorial additions, `<supplied>` or `<corr>` should be used. Marginalia supplied by later hands is assumed to be an addition by the identification of its hand and does not need to be tagged as such.

### Attributes for `<add>`:

* `@place`: Designates the point at which the addition is made. The [*Piers Plowman Electronic Archive*](http://www3.iath.virginia.edu/seenet/piers/protocoltran.html) uses only the following values: “inline”, “supralinear”, “sublinear”, “marginLeft”, “marginRight”, “topLeft”, “topCenter”, “topRight”, “bottomLeft”, “bottomCenter”, and “bottomRight”.
* `@hand`: Identifies the scribe who made the addition.
* `@resp`: Identifies the editor or transcriber who identified the hand. The default will be the initials of the named editor(s) as they appear in the `<teiHeader>`, and need not be recorded.
* `@cert`: Signifies the transcriber’s degree of certainty as to the identification of the hand.

The `<add>` tag is used for short sequences of text, single words, or phrases. `<addSpan/>` must be used for larger level additions because `<add>` tags do not carry over structural boundaries like `</l>`. `<addSpan/>` has the same attributes as `<add>`, with the addition of the attribute `@spanTo`, which refers to the spot where the added material ends. (There is also the possibility of using the attribute `@type`, but that would be used only if the added text is not on an original manuscript page.) Instead of the expected closing tag, `<addSpan/>` tags are bounded by an `<anchor/>` tag placed at the end of the span of added text. The `<anchor/>` element must have a valid `@xml:id` and should additionally contain `@type="addSpan"`.
