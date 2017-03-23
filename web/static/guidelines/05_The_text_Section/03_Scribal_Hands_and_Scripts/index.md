# Scribal Hands and Scripts

Full descriptions of scribal hands and scripts should be provided in the `<handDesc>` and `<scriptDesc>` sections of the `<teiHeader>`. AEME maintains a list of scribal hands in its named entities file. Since the names of most scribes are unknown, the `@xml:id` of a scribal hand will typically be something like `#bioUN0019`.  Scripts should similarly be given an `@xml:id` for cross-reference, and AEME should maintain a global list of these IDs.

Within the text transcription, elements or spans of elements can be identified with individual hands or scripts using `@hand` and `<handShift/>`. Identifications of scribal and hand script are by default considered to be of high certainty. Lower levels of certainty may be indicated by the use of `@cert[high|medium|low]`.

`@hand` and `<handShift/>` are primarily of use for search purposes since individual scripts and scribal hands are not represented with graphic cues in the diplomatic and critical views. Therefore, encoded identifiers of scribal hands and changes of script should be accompanied by editorial notes to identify on the front end views where changes of scribal hand occur.

The following standard reference works on the identification of scripts may be useful:

1. Brown, Michelle P. *A Guide to Western Historical Scripts from Antiquity to 1600*. London: The British Library, 1990.
2. Parkes, M. B. *English Cursive Book Hands, 1250-1500*. Oxford: Clarendon, 1969.
3. Preston, Jean F., and Laetitia Yeandle. *English Handwriting, 1400-1650: An Introductory Manual*. Binghamton, N.Y.: Medieval & Renaissance Texts & Studies, 1992.
4. Wright, Cyril Ernest. *English Vernacular Hands from the Twelfth to the Fifteenth Centuries*. Oxford: Clarendon Press, 1960.
5. Roberts, Jane. *Guide to Scripts Used in English Writings up to 1500*. Revised edition. London: British Library, 2011.
