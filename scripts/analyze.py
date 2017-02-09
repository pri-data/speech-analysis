import sys
import glob

def main(input_dir, output_dir, func): 
    """
    Input dir:
        
    """
    if func == 'word_length':
        word_length()




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
   main(sys.argv[1], sys.argv[2], sys.argv[3])