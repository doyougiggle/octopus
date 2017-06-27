# octopus
text-to-dep parse rep 

The system it is configured to run on the server called cognac under Python3.5
The script as per June 27 2017:
python tag_and_parse.py --infile /full/path/to/the/file --language en/fr/es/de (default en)

e.g.
python tag_and_parse.py --infile /projdata/alpage2/hmartine/proj/octopus/data/dummytext.txt
generates 
/projdata/alpage2/hmartine/proj/octopus/data/dummytext.txt.parsed


### Principles


### Getting started


### API documentation

POST /parse

```json
{
   "text": "This is the text I want to analyse",  
   "lang": "en"
}
```

