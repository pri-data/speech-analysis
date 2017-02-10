import pandas
import glob
from os.path import basename
import re

inquirer = pandas.read_csv("../data/inquirer-basic/inquirerbasicttabsclean", sep="\t")
for category in inquirer.columns[2:]:
    inquirer.Entry[inquirer[category].notnull()].to_csv('../data/dictionaries/' + category + '.csv', index=False)