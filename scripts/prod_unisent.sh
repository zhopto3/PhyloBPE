#!/bin/bash
#Zach Hopton
modeldir=./data/bpe_models
outdir=./data/tokenized_corpora
indir=./data/unisent_clean

#Make header for the final language vector file
echo -e 'lang\tavg_p\tavg_cf\tavg_i\tavg_h\tavg_r' > ./data/text_stats/lang_vecs_unisent.tsv
for file in $(ls $indir)
do
    echo "now processing $file"
    #Train a bpe tokenizer to carry out 200 merges
    subword-nmt learn-bpe -s 200 < $indir/$file > $modeldir/${file}.unisent.model
    #apply the bpe tokenizer to the clean corpus
    subword-nmt apply-bpe -c $modeldir/${file}.unisent.model < ./data/bibles_clean/$file > $outdir/unisent_tokenized_$file

    #Get rid of white space between the tokens
    sed -i -e 's/@@ /@@/g' $outdir/unisent_tokenized_$file
    rm $outdir/unisent_tokenized_$file-e

    #Collect type frequencies using script from Gutierrez-Vasques et al. 2023
    python3 ./scripts/freq_productivity.py $outdir/unisent_tokenized_$file
    #Calculate productivity, idiosyncrasy, and cumulative frequency for all the subword tokens
    python3 ./scripts/productivity.py $modeldir/${file}.unisent.model $outdir/unisent_tokenized_$file.freqsprod.tsv > ./data/text_stats/unisent_detailed_${file}

    # #As in original script, filter the detailed information away for a summary (https://github.com/ximenina/BPEProductivity/blob/master/scripts/2BPEproductivity_merges.sh)
    # #Filter only the summary of subwords:
	cat ./data/text_stats/unisent_detailed_${file}| grep "subword:" > ./data/text_stats/unisent_summary_${file}

    #Prepare tsv version
    echo -e 'subword\tprod\tcum_freq\tidiosyncrasy_index'  > ./data/text_stats/unisent_summary_${file}.tsv
    sed 's/subword://g; s/productivity://g; s/cum_freq://g; s/idiosyncrasy://g' ./data/text_stats/unisent_summary_${file} >>./data/text_stats/unisent_summary_${file}.tsv
    #delete text version
    rm ./data/text_stats/unisent_summary_${file}

    #Get subword probabilities for calculating entropy and redundancy of a corpus
    python3 ./scripts/freq.py $outdir/unisent_tokenized_$file
    #Calculate the Redundancy and Entropy of the tokenized corpora
    echo -e 'types\ttokens\tttr\tentropy\tredundancy' > ./data/text_stats/unisent_hr_${file}.tsv
    python3 ./scripts/measures_fromlist.py $outdir/unisent_tokenized_$file.freqs.tsv >> ./data/text_stats/unisent_hr_${file}.tsv
    #Write a script that avgs p,i,and cf, then puts it in a script w the entropy and redundancy. One line per lang.
    python3 ./scripts/avg_stats.py $file  >> ./data/text_stats/lang_vecs_unisent.tsv
done

#standardize each element of the language vectors to facilitate cross-lingual comparison
python3 ./scripts/standardize.py ./data/text_stats/lang_vecs_unisent.tsv ./data/text_stats/lang_vecs_unisent_standardized.tsv