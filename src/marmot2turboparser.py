import argparse

def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", help="train folder for each task") # allow multiple train files, each asociated with a task = position in the list
    args = parser.parse_args()
    fout = open(args.infile+".src2",mode="w",encoding="utf-8")

    for line in open(args.infile,encoding="utf-8"):
        line = line.strip()
        if line:
            """3       going   _       _       _       VERB    _       _"""
            idx,form,_,_,_,pos,_,_ = line.split("\t")
            outline = ["_"] * 10
            outline[0] = idx
            outline[1] = form
            outline[2] = form
            outline[3] = pos
            outline[4] = pos
            out="\t".join(outline)+"\n"
            fout.write(out)
        else:
            fout.write("\n")


if __name__=="__main__":
    main()
