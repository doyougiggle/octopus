import argparse

def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", help="train folder for each task")
    parser.add_argument("--wordmode",choices=["form","lemma"],default="form")
    parser.add_argument("--posmode",choices=["upos","petrov"],default="upos")

    # allow multiple train files, each asociated with a task = position in the list
    args = parser.parse_args()

    """7	individuals	individual	NOUN	NNS	Number=Plur	5	obj	_	_"""


    petrov = dict()
    petrov["ADJ"] = "ADJ"
    petrov["ADP"] = "ADP"
    petrov["ADV"] = "ADV"
    petrov["AUX"] = "VERB"
    petrov["CCONJ"] = "CONJ"
    petrov["DET"] = "DET"
    petrov["INTJ"] = "X"
    petrov["NOUN"] = "NOUN"
    petrov["NUM"] = "NUM"
    petrov["PART"] = "PRT"
    petrov["PRON"] = "PRON"
    petrov["PROPN"] = "NOUN"
    petrov["PUNCT"] = "."
    petrov["SCONJ"] = "CONJ"
    petrov["SYM"] = "X"
    petrov["VERB"] = "VERB"
    petrov["X"] = "X"

    for line in open(args.infile):
        line = line.strip()
        if line:
            idx,form,lemma,upos,oldpos,feats,head,label,e1,e2 = line.split("\t")

            if args.wordmode == 'form':
                outword = form
            else:
                outword = lemma

            if args.posmode == 'upos':
                outpos = upos
            else:
                outpos = petrov[upos]

            if outword.startswith("REPLACE_"):
                outword = lemma
                outpos = "PRON"

            outline = ["_"] * 10
            outline[0] = idx
            outline[1] = outword
            outline[2] = outword
            outline[3] = outpos
            outline[4] = outpos
            outline[6] = head
            outline[7] = label
            print("\t".join(outline))
        else:
            print()


if __name__=="__main__":
    main()
