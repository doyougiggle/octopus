import argparse
import os
import random
import string
import subprocess

import sys
from nltk.tokenize import WordPunctTokenizer, StanfordTokenizer


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


stanfordpath = "lib/stanford-postagger-2017-06-09/stanford-postagger.jar"
stanfordpath = None


def instance_tokenizer(language, stanfordpath=None):
    # you can add more params or kinds of tokenizer from here:
    # http://www.nltk.org/api/nltk.tokenize.html
    if stanfordpath:
        tok = StanfordTokenizer(path_to_jar=stanfordpath)
    else:
        tok = WordPunctTokenizer()

    return tok


def marmot2turboparser(temphandle):
    outfile = temphandle + ".toparse"
    infile = temphandle + ".tok.pos"
    fout = open(outfile, mode="w", encoding="utf-8")

    for line in open(infile, encoding="utf-8"):
        line = line.strip()
        if line:
            """3       going   _       _       _       VERB    _       _"""
            idx, form, _, _, _, pos, _, _ = line.split("\t")
            outline = ["_"] * 10
            outline[0] = idx
            outline[1] = form
            outline[2] = form
            outline[3] = pos
            outline[4] = pos
            out = "\t".join(outline) + "\n"
            fout.write(out)
        else:
            fout.write("\n")
    fout.close()
    return outfile


def sentences2tokens(infile, temphandle, tok):
    outfile = temphandle + ".tok"
    fout_tokenized = open(outfile, mode="w")

    for line in open(infile).readlines():
        lineout = "\n".join(tok.tokenize(line)) + "\n\n"
        fout_tokenized.write(lineout)
    fout_tokenized.close()
    return outfile


def main():
    parser = argparse.ArgumentParser(description="""Tagger+Parser""")
    parser.add_argument("--infile", help="Input file")
    parser.add_argument("--outfile", help="Output file, default is ${inputfile}.parsed")
    parser.add_argument("--language", default="en", type=str, help="Language, default=en")
    parser.add_argument("--temp_path", default="/tmp", help="Temporary directory, default=/tmp")
    args = parser.parse_args()

    # Validating input
    if not args.infile:
        print("Missing the input file to be processed. \n")
        parser.print_help()
        sys.exit(-1)

    # NB!! the current code assumes sentence per line. We might need to add segmentation.
    # DONE tokenize plaintext in args.infile -- pending, include lang parameter or backoff to whitespace otherwise
    # TODO convert Marmout output to Parser input, namely F.temp2 -- implemented, need to include
    # TODO parse F.temp2, yielding F.parse -- train three models, and determine which one to actually use
    # TODO remove F.temp and F.temp2

    print("processing...")

    temphandle = args.temp_path + "/octo_" + id_generator()
    parsemodel = "/projdata/alpage2/hmartine/tools/" + args.language + "_form_upos.turbomodel_svm_mira/" + args.language + "_train_form_upos.conll.model"
    tok = instance_tokenizer(args.language, stanfordpath)
    file_to_tag = sentences2tokens(args.infile, temphandle, tok)

    os.chdir("/projdata/alpage2/hmartine/tools/marmot")
    subprocess.call(
        ("bash tag_with_marmot.sh " + args.language + " " + file_to_tag).split())  # the output of this will add .pos
    # os.popen("cd -")
    file_to_parse = marmot2turboparser(temphandle)
    os.chdir("/projdata/alpage2/hmartine/tools")
    subprocess.call(("bash parse_with_turboparser.sh " + file_to_parse + " " + parsemodel).split())  # the output of this will add .pos
    subprocess.call(["mv", file_to_parse + ".parsed", args.infile + ".parsed"])
    subprocess.call(["rm", file_to_parse])
    subprocess.call(["rm", file_to_tag])


if __name__ == "__main__":
    main()

# what follows is the original bash that fulfilled the task of this present Python script, saved for reference

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
