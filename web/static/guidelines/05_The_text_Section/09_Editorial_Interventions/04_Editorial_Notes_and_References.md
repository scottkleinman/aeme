# Editorial Notes and References

Editorial notes are indicated with the `<note>` tag and a pointer to the `@xml:id` of the element to which the note is attached. All notes must also be assigned an `@xml:id` number, and we will need to come up with a convention for naming note IDs, as well as our system of coordinating with the element to which the note refers. `@xml:id` values should be formed with room to expand: e.g. `ed0001`, `ed0002`, etc. They need not be human-readable within a line; we will want human readability for `@target` and `@targetEnd` if we use them coordinate. For example: `<note xml:id="ed0001" target="#ch0001" targetEnd="#pt0001"/>` links to `<anchor xml:id="ch0001"/>` and `<ptr xml:id="pt0001"/>`.

AEME requires the use of `@type` to indicate for all critical notes. The current taxonomy, derived from the <a href="http://www3.iath.virginia.edu/seenet/piers/protocoltran.html" target="_blank">*Piers Plowman Electronic Archive*</a>, consists of the following values: “cod”, “pal”, “ling”, “lex”, “hist”, “src”, “theo”, “text”, “enc” (short names for “codicological”, “paleographic”, “linguistic”, “lexical”, “historical”, “source”, “theological”, “textual”, and “encoding”). Note that the boundaries between “ling” and “lex”, “hist” and “theo” may be somewhat hard to determine. It is possible to encode multiple note types.

Individual note types will be displayed in the following views:
* cod: facsimile, diplomatic
* pal: facsimile, diplomatic
* ling: critical
* lex: critical
* hist: critical
* src: critical
* theo: critical
* enc: None, purely for commentary on encoding decisions and issues.

The additional codes “facs”, “dipl”, and “crit” can be used with `@rend to override the default views. For instance, `<note type="ling" rend="dipl crit">` would appear in the diplomatic view, as well as the critical view. Although an unlikely scenario, the formulation `<note type="ling" rend="dipl">` could be used to force a linguistic note to appear only in the diplomatic view.

Cross-references within the text may be indicated with the `<ref>` element. However, it must be clearly indicated that the reference is editorial by some means, such as inclusion of the `<ref>` inside the text of an editorial note.
