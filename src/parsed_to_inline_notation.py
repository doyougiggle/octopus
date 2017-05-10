import argparse


def outlists(L):
    print("\t".join([" ".join(l) for l in L]))
def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", help="")
    parser.add_argument("--column", help="",default=3,type=int)
    args = parser.parse_args()


    """2	probably	probably	ADV	ADV	_	3	advmod"""
    tags, heads, labels, words = [],[],[],["root_node"]
    for line in open(args.infile):
        line = line.strip()
        if line:
            idx,w1,w2,p1,p2,m,h,l = line.split("\t")
            tags.append(p1)
            heads.append(h)
            labels.append(l)
            words.append(w1)
        else:
            head_for_each_word = [words[int(h)] for h in heads]
            outlists([tags, heads, labels, head_for_each_word])
            tags, heads, labels, words = [], [], [], ["root_node"]

    if tags:
        #silly variable names, here I store all words because it is comfy
        head_for_each_word =  [words[int(h)] for h in heads]
        outlists([tags, heads, labels,head_for_each_word])


if __name__=="__main__":
    main()
