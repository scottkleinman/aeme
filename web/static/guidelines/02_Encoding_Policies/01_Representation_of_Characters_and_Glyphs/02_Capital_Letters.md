# Capital Letters

Capitalisation in medieval manuscripts can be ambiguous, as letter height and shape are not always reliable indicators. Therefore, AEME policy leaves considerable latitude for editorial discretion.
AEME policy is to represent verse-initial letters as capitals in the critical view, regardless of whether they are capitalised in the diplomatic view. The distinction should be formally encoded using the `<choice>`, `<orig>`, and `<reg>` elements. For example:

```xml
<choice>
    <orig>herkne&thorn;</orig>
    <reg>Herkne&thorn;</reg>
</choice> to me gode men
```

This will render as “herkneþ to me gode men” in the diplomatic view but “Herkneþ to me gode men” in the critical view.

Sentence initial letters and proper names may be similarly distinguished in the diplomatic and critical views. Likewise, letters capitalised in the manuscript may be rendered lowercase—following modern typographic practices—in the critical view at the editor’s discretion. Editors should document their policy on capitalisation in the `<teiHeader>` and follow it consistently.
