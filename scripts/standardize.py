import sys

import pandas as pd
from scipy.stats import zscore


def main(in_path,out_path):
    lang_vecs = pd.read_csv(in_path,delimiter='\t')

    lang_vecs["standardized_p"] = zscore(lang_vecs['avg_p'])
    lang_vecs['standardized_cf']=zscore(lang_vecs['avg_cf'])
    lang_vecs['standardized_i']=zscore(lang_vecs['avg_i'])
    lang_vecs['standardized_h']=zscore(lang_vecs['avg_h'])
    lang_vecs['standardized_r']=zscore(lang_vecs['avg_r'])

    lang_vecs.drop(labels=['avg_p','avg_cf','avg_i','avg_h','avg_r'],inplace=True,axis=1)
    lang_vecs.to_csv(out_path, sep='\t',index=False, encoding="utf-8")


if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])