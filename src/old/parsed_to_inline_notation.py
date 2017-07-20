

import argparse


def outlists(L,fout):
    w = "\t".join([" ".join(l) for l in L])+"\n"
    fout.write(w)

def main():
    parser = argparse.ArgumentParser(description=""" Parser output conversion for convenience reasons""")
    parser.add_argument("--infile", help="")
    parser.add_argument("--outfile", help="")
    parser.add_argument("--column", help="",default=3,type=int)
    args = parser.parse_args()

    fout = open(args.outfile,mode="w",encoding="utf-8")

    """2	probably	probably	ADV	ADV	_	3	advmod"""
    tags, heads, labels, words = [],[],[],["root_node"]
    for line in open(args.infile,encoding="utf-8"):
        line = line.strip()
        if line:
            idx,w1,w2,p1,p2,m,h,l = line.split("\t")
            tags.append(p1)
            heads.append(h)
            labels.append(l)
            words.append(w1)
        else:
            head_for_each_word = [words[int(h)] for h in heads]
            outlists([tags, heads, labels, head_for_each_word],fout)
            tags, heads, labels, words = [], [], [], ["root_node"]

    if tags:
        #silly variable names, here I store all words because it is comfy
        head_for_each_word =  [words[int(h)] for h in heads]
        outlists([tags, heads, labels,head_for_each_word],fout)

    fout.close()

if __name__=="__main__":
    main()
