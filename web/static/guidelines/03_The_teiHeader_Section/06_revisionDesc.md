The optional `<revisionDesc>` is required once a document file has been updated after an initial commit. Changes are recorded using `<change who="" when="">`, with a description of the change inside the `<change>` element. For example:

```xml
<revisionDesc>
    <change who="#bioKL0001" when="2014-01-01">Corrected reading of ... </change>
</revisionDesc>
```

### AEME Requirements

Dates should be given in the format `YYYY-MM-DD`. Each successive change should be recorded as an additional `<change>` element. `@who` should record the `@xml:id` of the person responsible for the change.

`<change>` should be used only if we add or re-work a significant section (more incidental changes will be recorded by git). When the text is ready for publication, changes should be removed. After publication, all further changes should be recorded.
