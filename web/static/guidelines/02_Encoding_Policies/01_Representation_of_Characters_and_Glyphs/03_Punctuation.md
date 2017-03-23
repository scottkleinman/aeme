# Punctuation

Medieval punctuation marks should be encoded using appropriate entity representations (numeric or aliased). Entities for many common medieval punctuation marks are listed in AEME’s `Character_Entities.xlsx` spreadsheet.

It is common practice in modern editions to replace medieval punctuation marks with common “equivalents” (that is, modern symbols that the editor deems to be an acceptable substitute). It is also common to introduce modern punctuation marks to aid the modern reader in parsing the syntactic (or sometimes metrical) structure of the text. These practices should only ever take place in the critical view and should be formally separated from diplomatic markup as described below. Editors should document their policy on editorially supplied punctuation in the `<teiHeader>` and follow it consistently.

The AEME schema incorporates the `<pc>` element from the TEI Analysis module to identify non-editorially supplied punctuation. All untagged punctuation is assumed to be supplied by the modern editor for display in the critical view only. Where a punctuation mark in the diplomatic view is to be rendered differently in the critical view, the critical reading should be placed in `@rend`. The following examples illustrate usage.

```xml
<!-- Punctuation in Diplomatic View only -->
Some text<pc>&punctelev;</pc> and some more text

<!-- Same Punctuation in Diplomatic and Critical Views -->
Some text<pc rend=".">.</pc>

<!-- Different Punctuation in Diplomatic and Critical Views -->
Some text<pc rend=",">&punctelev;</pc> and some more text

<!-- Punctuation in Critical View only -->
Some text, and some more text
```

Note that the scenario in which a modern punctuation mark is to replace a medieval punctuation mark in the critical view presents a minor processing difficulty if the medieval symbol is preceded by space. This is not the convention in modern typography. The easiest solution is to delete white space before medieval punctuation marks (and therefore before `<pc>` in the encoding), as demonstrated in the examples above. For this practice in a diplomatic edition, see M.J. Driscoll, “Electronic Textual Editing: Levels of Transcription”, in Unsworth, O’Brien O’Keeffe, and Burnard, *Electronic Textual Editing* (http://www.tei-c.org/About/Archive_new/ETE/Preview/driscoll.xml). In certain cases, the editor may wish to preserve white space before a punctuation mark in the diplomatic view. In these cases, AEME recommends embedding the space within `<pc>`. For instance, one might wish to preserve the space around a *punctus elevatus* marking a caesura. This would be encoded as

```xml
Some text<pc> &punctelev;</pc> and some more text
```

`<pc>` may also take `@type="caesura"` to indicate that the punctuation mark represents a half-line divider. In this case, no internal space is required because we can achieve the same effect by styling elements of this type with a margin on either side. The code would then look like this:

```xml
<pc type="caesura">&punctelev;</pc>
```

Currently, the use of `@type="caesura"` is optional in AEME editions. No other possible values for `@type` have been proposed.