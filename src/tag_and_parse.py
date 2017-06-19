import argparse

def main():
    parser = argparse.ArgumentParser(description="""Tagger+Parser""")
    parser.add_argument("--infile", help="")
    parser.add_argument("--outfile", help="")
    parser.add_argument("--language", help="",default="en",type=str)
    args = parser.parse_args()

    #TODO tokenize plaintext in args.infile -- pending, include lang parameter or backoff to whitespace otherwise
    #TODO save tokenized to F.temp
    #TODO tag F.temp with Marmot, yielding F.pos that has tags
    #TODO convert Marmout output to Parser input, namely F.temp2 -- implemented, need to include
    #TODO parse F.temp2, yielding F.parse -- train three models, and determine which one to actually use
    #TODO remove F.temp and F.temp2

if __name__=="__main__":
    main()



#what follows is the original bash that fulfilled the task of this present Python script, saved for reference

"""#!/usr/bin/env bash
file=$1
model=$2
lang=$3

python discodata_source_2marmot.py --infile $file --outfile  $file.src  #> $file.src
cd /projdata/alpage2/hmartine/tools/marmot
bash tag_with_marmot.sh  $lang $file.src
cd -
python marmot2turboparser.py --infile $file.src.pos --outfile  $file.src2
cd /projdata/alpage2/hmartine/tools
bash parse_with_turboparser.sh $file.src2 $model
cd -
python parsed_to_inline_notation.py --infile $file.src2.parsed --outfile $file.src.inline
"""