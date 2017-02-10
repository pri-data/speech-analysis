"""
For ea. speech:
* For each category from the Harvard inquirer:
   * output WORD_COUNT, NUMBER OF MATCHES for that category
"""
import pandas  
import glob
from os.path import basename 
import re
import sys
from collections import Counter
import csv

def main(path_to_dictionaries, path_to_tokens, path_to_results):

    dictionaries = glob.glob(path_to_dictionaries + '*')
    speeches = glob.glob(path_to_tokens + '*') 
 
    categories = []
    for d in dictionaries:
        with open(d) as f:
            categories.append((basename(d).replace('.csv', ''), f.read().split()))

    print path_to_results
    outpath =  path_to_results + 'emotional-vocab-count.csv'

    print outpath
    with open(outpath, "wb") as outfile: 
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL) 
        #writer.writerow(['president', 'year', 'category', 'count', 'total_words', 'percent'])
        writer.writerow(['speech', 'category', 'count', 'total_words', 'percent'])

        for s in speeches:
            speechname = basename(s).replace("-tokens.txt", "")  

            with open(s) as f:
                tokens = f.read().upper().split() 
                c = Counter(tokens)

                for category in categories:
                    total = len({key: c[key] for key in c if key in category[1]}.values())
                    wc = len(tokens)
                    percent = 100 * (total / (wc * 1.0))
                    writer.writerow([speechname, category[0], total, wc, round(percent,2)])
 
    # still easier than sorting in excel
    df = pandas.read_csv(outpath)
    df.sort_values(['category', 'percent'], ascending=[True,False])\
                    .to_csv(outpath.replace('.csv', '-SORTED.csv'), index=False)


if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2], sys.argv[3])
   # example: 
   # python count_emot.py ../data/dictionaries/ ../data/tokenized/SOTU/ ../results/SOTU/
   # python count_emot.py ../data/dictionaries/ ../data/tokenized/trump-speeches/ ../results/trump-speeches/


