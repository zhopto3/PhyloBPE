import os
import unicodedata

import pandas as pd

#Had to remove scots gaelic bc not available
#Had to remove romani bc of lack of variety specification
ISOS = {'afr':'Afrikaans','sqi':'Albanian','hye':'Armenian',
        'bul':'Bulgarian','ces':'Czech','dan':'Danish',
        'nld':'Dutch','eng':'English','pes':'Farsi',
        'fra':"French",'deu':"German",
        'ell':"Greek",'hin':"Hindi", 'guj':"Gujarati",
        'isl':"Icelandic",'ita':"Italian",'lav':"Latvian",
        'lit':"Lithuanian",'mar':"Marathi",'npi':"Nepali",
        'nob':"Norwegian",'pol':"Polish",'por':"Portuguese",
        'ron':'Romanian','rus':"Russian",
        'srp':"Serbian",'slk':"Slovak",'slv':'Slovene',
        'spa':'Spanish','swe':"Swedish",'ukr':"Ukranian"}


def main():
    #get the relevant word list
    for f in os.listdir("./data/unisent"):
        if ".DS" not in f:
            df = pd.read_csv(f"./data/unisent/{f}",delimiter="\t",header=None,encoding="utf-8")
            df = df[0]
            out_name=f"./data/unisent_clean/{ISOS[f.split("_")[0]]}_clean.txt"
            out_list = df.to_list()

            with open(out_name,"w",encoding='utf-8') as f_out:
                for term in out_list:
                    term = unicodedata.normalize("NFKC",term)
                    f_out.write(term+"\n")


if __name__=="__main__":
    main()