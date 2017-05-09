import argparse


def outlists(L):
    print("\t".join([" ".join(l) for l in L]))
def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", help="")
    parser.add_argument("--column", help="",default=3,type=int)
    args = parser.parse_args()


    """2	probably	probably	ADV	ADV	_	3	advmod"""
    tags, heads, labels = [],[],[]
    for line in open(args.infile):
        line = line.strip()
        if line:
            idx,w1,w2,p1,p2,m,h,l = line.split("\t")
            tags.append(p1)
            heads.append(h)
            labels.append(l)
        else:
            outlists([tags,heads,labels])
            tags, heads, labels = [], [], []

    if tags:
        outlists([tags, heads, labels])


if __name__=="__main__":
    main()
