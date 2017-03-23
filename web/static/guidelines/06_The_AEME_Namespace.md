# The AEME Namespace

Where the TEI Guidelines do not give elements or attributes appropriate to the project, new ones may be added through the custom AEME schema. In TEI P5, any additions of this type should be defined as a namespace in the xml root element:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:aeme="http://aeme.emesoc.org/ns/1.0">
...
</TEI>
```

The namespace is included in the template file structure provided in the [Document File Structure](01_Editing_Policies/07_Document_File_Structure) section.
