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

def main(dictionaries_dir="/Users/sophie_chou/Google Drive/Speech Analyses/speech-analysis/data/dictionaries/", \
            speeches_dir='/Users/sophie_chou/Google Drive/Speech Analyses/speech-analysis/data/tokenized/SOTU/',\
            results_dir="/Users/sophie_chou/Google Drive/Speech Analyses/speech-analysis/results/SOTU/"): 

    dictionaries = glob.glob(dictionaries_dir + '*')
    speeches = glob.glob(speeches_dir + '*') 
 
    categories = []
    for d in dictionaries:
        with open(d) as f:
            categories.append((basename(d).replace('.csv', ''), f.read().split()))

    print results_dir
    outpath =  results_dir + 'emotional-vocab-count.csv'

    print outpath
    with open(outpath, "wb") as outfile: 
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL) 
        writer.writerow(['president', 'year', 'category', 'count', 'total_words', 'percent'])

        for s in speeches:
            president, year = basename(s).replace("-tokens.txt", "").split("-")
            print president, year

            with open(s) as f:
                tokens = f.read().upper().split() 
                c = Counter(tokens)

                for category in categories:
                    total = len({key: c[key] for key in c if key in category[1]}.values())
                    wc = len(tokens)
                    percent = 100 * (total / (wc * 1.0))
                    writer.writerow([president, year, category[0], total, wc, round(percent,2)])
 
    # still easier than sorting in excel
    df = pandas.read_csv(outpath)
    df.sort_values(['category', 'percent'], ascending=[True,False])\
                    .to_csv(outpath.replace('.csv', '-SORTED.csv'), index=False)


if __name__ == "__main__":
   main()


