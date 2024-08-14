"""A script to compile the text statistics and aggregate them for a given language
Zach Hopton
"""
import sys

import pandas as pd


def get_prod_avgs(path):
    df=pd.read_csv(path,delimiter="\t",encoding="utf-8")
    avg_p = df['prod'].mean()
    avg_cf = df['cum_freq'].mean()
    avg_i = df['idiosyncrasy_index'].mean()

    return avg_p,avg_cf,avg_i


def get_ent(path):
    df=pd.read_csv(path,delimiter="\t",encoding="utf-8")
    return (df.loc[0,'entropy'],df.loc[0,'redundancy'])


def main(lang_file):
    prod_path=f"./data/text_stats/summary_{lang_file}.tsv"
    hr_path=f"./data/text_stats/hr_{lang_file}.tsv"

    avg_p,avg_cf,avg_i=get_prod_avgs(prod_path)

    h,r = get_ent(hr_path)

    lang = lang_file.split(".")[0]
    print(*[lang,avg_p,avg_cf,avg_i,h,r],sep="\t")

if __name__=="__main__":
    main(sys.argv[1])
