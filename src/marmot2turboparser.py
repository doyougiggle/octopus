import argparse

def main():
    parser = argparse.ArgumentParser(description="""Run the NN tagger""")
    parser.add_argument("--infile", nargs='*', help="train folder for each task") # allow multiple train files, each asociated with a task = position in the list
    args = parser.parse_args()



if __name__=="__main__":
    main()
