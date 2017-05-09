import argparse

def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", help="")
    parser.add_argument("--column", help="",default=2,type=int)
    args = parser.parse_args()

    #you	you|PRON	Woran denken Sie , wenn ich das Wort " Design " sage ?	What|PRON do|VERB REPLACE_2 think|VERB of|ADP when|ADV I|PRON say|VERB the|DET word|NOUN "|. design|NOUN "|. ?|.	0-0 1-3 2-2 4-5 5-6 6-8 7-9 8-10 9-11 10-12 11-7 12-13	2039
    #form  form|POS   Tokenized text in the Source   Token|POS for|POS Target|POS alignments_that_I_ignore INDEX
    for line in open(args.infile):
        blocks= line.split("\t")
        forms = blocks[args.column]
        print("\n".join(forms))
        print("")

if __name__=="__main__":
    main()
