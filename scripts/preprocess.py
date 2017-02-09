"""
scripts to clean, tokenize, remove stopwords
"""

import sys
import glob
# Make your word tokenizer. We don't care about punct.
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+') 

def main(input_dir, output_dir): 
    """
    input_dir:
        path to directory that holds text files of speeches.
        1 file per speech, unprocessed.
    output_dir:
        where cleaned, tokenized, stopword removed speeches go
    """
    


def preproc(input_dir):
    ""
    speeches = glob.glob(input_dir)
    for s in speeches:
        print basename(s)
        with open(s) as speech:
            text = speech.read()
            tokens = tokenizer.tokenize(text.lower())
            biglist.append([basename(s), tokens])


if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])