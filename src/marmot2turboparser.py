import argparse

def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", nargs='*', help="train folder for each task") # allow multiple train files, each asociated with a task = position in the list
    args = parser.parse_args()
    for line in open(args.infile):
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
            print("\t".join(outline))
        else:
            print()


if __name__=="__main__":
    main()
