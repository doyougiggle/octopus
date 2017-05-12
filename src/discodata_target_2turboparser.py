import argparse

def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", help="")
    parser.add_argument("--column", help="",default=3,type=int)
    parser.add_argument("--outfile", help="")

    args = parser.parse_args()

    #you	you|PRON	Woran denken Sie , wenn ich das Wort " Design " sage ?	What|PRON do|VERB REPLACE_2 think|VERB of|ADP when|ADV I|PRON say|VERB the|DET word|NOUN "|. design|NOUN "|. ?|.	0-0 1-3 2-2 4-5 5-6 6-8 7-9 8-10 9-11 10-12 11-7 12-13	2039
    #form  form|POS   Tokenized text in the Source   Token|POS for|POS Target|POS alignments_that_I_ignore INDEX

    fout = open(args.outfile,mode="w",encoding="utf-8")
    for line in open(args.infile,encoding="utf-8"):
        blocks= line.split("\t")
        target_with_pos = blocks[args.column]
        for idx,token in enumerate(target_with_pos.split(" ")):
            outline = ["_"] * 10
            lemma =""
            pos = ""
            if token.startswith("REPLACE_"):
                lemma = token
                pos = "PRON"
            else:
                try:
                    lemma, pos = token.split("|")
                except:
                    print(token)
            outline[0] = str(idx+1)
            outline[1] = lemma
            outline[2] = lemma
            outline[3] = pos
            outline[4] = pos
            out="\t".join(outline)+"\n"
            fout.write(out)
            fout.write("\n")
    fout.close()


if __name__=="__main__":
    main()
