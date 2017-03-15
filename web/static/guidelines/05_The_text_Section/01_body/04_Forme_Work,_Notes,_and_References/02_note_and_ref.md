`<note>` may be used either for critical notes or for transcribed notes in the manuscript. The discussion here relates to transcribed notes and references rather than those supplied by the editor. For the latter, see the section on [Editorial Notes and References](../../Editorial_Interventions/Editorial_Notes_and_References).

Transcribed notes are placed in the XML at the end of the `div` element to which they pertain, gathered within a child numbered `div`. A `<note>` element should contain `@target` pointing to a `<anchor/>` element in the text. For instance, `<note target="#32">` would point to `<anchor xml:id="32"/>` or `<ptr xml:id="32"/>`.
Transcribed notes can also have other attributes such as `@place`, `@type`, and `@subtype` to indicate the type of note and its location in the *mise-en-page*. For instance, `<note type="gloss" place="margin-right">A note</note>` would indicate a note in the right margin. AEME has not yet developed a taxonomy of note types.

References are often biblical references or names of kings, placed in the margin. They may be indicated using the `<ref>` element with attributes similar to those used for `<note>`.
