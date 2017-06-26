import argparse,string, random, os

from nltk.tokenize import WordPunctTokenizer, StanfordTokenizer

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

stanfordpath = "/projdata/alpage2/hmartine/proj/octopus/util/stanford-postagger-2017-06-09/stanford-postagger.jar"
stanfordpath = None

def instance_tokenizer(language, stanfordpath=None):

    #you can add more params or kinds of tokenizer from here:
    #http://www.nltk.org/api/nltk.tokenize.html
    if stanfordpath:
        tok = StanfordTokenizer(path_to_jar=stanfordpath)
    else:
        tok = WordPunctTokenizer()

    return tok


def main():
    parser = argparse.ArgumentParser(description="""Tagger+Parser""")
    parser.add_argument("--infile", default="/Users/hmartine/proj/octopus/data/dummytext.txt")
    parser.add_argument("--outfile", default="")
    parser.add_argument("--language", default="en",type=str)
    parser.add_argument("--temp_path",default=".")
    args = parser.parse_args()

    #NB!! the current code assumes sentence per line. We might need to add segmentation.
    #DONE tokenize plaintext in args.infile -- pending, include lang parameter or backoff to whitespace otherwise
    #TODO convert Marmout output to Parser input, namely F.temp2 -- implemented, need to include
    #TODO parse F.temp2, yielding F.parse -- train three models, and determine which one to actually use
    #TODO remove F.temp and F.temp2

    print("processing...")

    temphandle = args.temp_path+"/octo_"+id_generator()
    fout_tokenized = open(temphandle+".tok",mode="w")
    marmotmodel = "/projdata/alpage2/hmartine/tools/marmot/"+args.language+posmodel.marmot

    #DONE save tokenized to F.temp
    tok = instance_tokenizer(args.language,stanfordpath)
    for line in open(args.infile).readlines():
        lineout = "\n".join(tok.tokenize(line))+"\n\n"
        fout_tokenized.write(lineout)
    fout_tokenized.close()
    #TODO tag F.temp with Marmot, yielding F.pos that has tags
    os.chdir("/projdata/alpage2/hmartine/tools/marmot")
    os.popen("bash tag_with_marmot.sh $"+args.language+" $"+temphandle+".tok $"+marmotmodel) #the output of this will add .pos
    #os.popen("cd -")
    #TODO turn marmot2turboparser.py - -infile $file.src.pos - -outfile  $file.src2 into function calls
    #subprocess.Popen("cd /projdata/alpage2/hmartine/tools")
    #subprocess.Popen("bash parse_with_turboparser.sh $"+filetoparse+" $"+parsemodel) #the output of this will add .pos
    #subprocess.Popen("cd -")


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