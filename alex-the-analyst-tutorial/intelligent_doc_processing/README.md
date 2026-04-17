Following along Alex the Analyst's [IDP Tutorial](https://www.youtube.com/watch?v=nizvj7xAwq8).

Explanation of the functionality: [Databricks IDP Blog](https://www.databricks.com/blog/pdfs-production-announcing-state-art-document-intelligence-databricks)

## Video 1 - Intro to IDP

#### Why IDP Matters
- Most data is unstructured
- Most critical information lives in the documents
- Manual processing does not scale
- Rules based parsing is fragile
- IDP enables faster, more reliable data workflows

#### Difference

- ##### Traditional
  - OCR + Rules
  - Regex + Templates
  - High Maintenance 
  - Breaks with format changes

- ##### IDP
  - Understand the layout and context of the document
  - Adapts to document filetype
  - Minimal manual changes


## Video 2 - AI_Parse_Document Function

#### AI_Parse
- Databricks SQL AI function for parsing unstructured documents
- Turns free text into HTML
- Works with both free text and tabular data
- Works with word, ppts, images and pdfs 