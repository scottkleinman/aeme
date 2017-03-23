# Distinguishing the Diplomatic and Critical Markup

Tags like `<supplied>`, `<sic>`, and `<corr>` inherently indicate editorial interventions, and their content will be displayed only in the critical view. Other types of content require a more nuanced approach. The `<choice>` element allows the two views to be formally separated. Typically, `<choice>` will contain an `<orig>` element, the content of which is the diplomatic representation, and a `<reg>` element, which represents the critical representation. In some cases, this formal separation requires some editorial decision-making. For instance, the word “Man”, when not at the beginning of a sentence or verse-line, may be tagged:

```xml
<choice>
	<orig>M</orig>
	<reg>m</reg>
</choice>an

or 

<choice>
	<orig>Man</orig>
	<reg>man</reg>
</choice>
```

That is, a decision is required as to whether to tag only the differing parts of the word or the word as a whole. The first example implies that the scribe was thinking in terms of letters (i.e. a capital letter would look nice here), whereas the second example implies that the scribe was thinking in terms of words (i.e. the word “man” has more semantic weight here). Although it is preferable for rendering purposes not to have stray characters outside of the `<choice>` element, as editors, we should adopt the method that best reflects our interpretation of the scribe’s thinking.

For specific editorial policies on the handling of capital letters and abbreviations in diplomatic and critical views, see the appropriate sections under [Word-Level Representations](/Encoding_Policies/Word-Level_Representations) above.
