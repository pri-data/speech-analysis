"""
scripts to clean, tokenize, remove stopwords
"""
import pandas
import sys 
import glob
from os.path import basename
# Make your word tokenizer. We don't care about punct.
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+') 

def main(input_dir='../data/SOTU/', output_dir='../data/tokenized/SOTU/'): 
    """
    input_dir:
        path to directory that holds text files of speeches.
        1 file per speech, unprocessed.
    output_dir:
        where cleaned, tokenized, stopword removed speeches go
    """
    preproc(input_dir, output_dir)
    

def preproc(input_dir, output_dir):  
    """
    input_dir:
        path to directory that holds text files of speeches.
        1 file per speech, unprocessed.
    output_dir:
        where cleaned, tokenized, stopword removed speeches go
    """
    biglist = []
    speeches = glob.glob(input_dir + '/*')
    for s in speeches:
        print basename(s)
        with open(s) as speech:
            text = speech.read()
            tokens = tokenizer.tokenize(text.lower())
            with open(output_dir + basename(s).replace(".txt","") + '-tokens.txt','wb') as resultFile:
                resultFile.write(" ".join(tokens))
            biglist.append([basename(s), tokens])

    df = pandas.DataFrame(biglist)
    df.columns = ['president', 'tokens'] 

    df = pandas.DataFrame(biglist)
    df.columns = ['president', 'tokens']


if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])

   # example: preprocess.py input_dir output_dir