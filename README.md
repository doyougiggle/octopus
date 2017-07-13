# octopus
text-to-dep parse rep

## Overview

This project depends on the following tools: 
 - Marmot (add url)
 - TurboParser (add url)
 
## Build and Run
1. We recommend you to use virtualenv 

2. Install the dependencies using
> pip install -r requirements.txt

3. Run it use the following command: 
> python tag_and_parse.py --infile /full/path/to/the/file --language en/fr/es/de (default en)

For example the command 
> python tag_and_parse.py --infile dummytext.txt

will output the results to `dummytext.txt.parsed`


### API documentation

POST /parse

```json
{
   "text": "This is the text I want to analyse",  
   "lang": "en"
}
```

