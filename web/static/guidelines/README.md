# README

Guidelines documentation should be written in Markdown.

All content is loaded with Ajax. Internal links should be provided in the form of the path inside the `guidelines` folder. The `.md` extension should be left off of the file name.

External links should be given in HTML in the form `<a href="path_to_website" target="_blank">Link Text</a>`.

The guidelines theme is based on the blue theme for [Daux](http://daux.io/). Menu links that do not load a page should be given the value `@href="#"`. Otherwise, their links should be the same as internal links within the article content.

The content has been indexed for Tipue search and is loaded from `tipuesearch_content.js`. The process of generating the JSON array is arduous, but the indexing is based on the original Markdown. Everything but the titles seems to render nicely in HTML. The implementation uses a slightly customised version of `tipue.js` and `tipue.css` so these files should be updated if Tipue search is ever updated. Tipue search seems to require the `GET` method, which adds a query string to the URL. Javascript is used to remove the query string when the user navigates away from the search results page. Note that it is possible that some pages have been missed in the indexing. This should be checked. Also, the `tipuesearch_set.js` file is the default one. This contains stop words and the like. It could use some customisation.
