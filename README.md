# PhyloBPE
Testing for phylogenetic signal in the BPE vocabulary of related languages from the Indo-European family. 
Authored Zachary W. Hopton for the final project in FS24 Statistical Modeling of Language Dynamics at the University of Zürich.

The following is a brief review of the contents in this GitHub Repository:

- data
    - bibles_clean: Bible texts (downloaded from https://github.com/christos-c/bible-corpus) after preprocessing
    - bpe_models: The langauge specific BPE models trained using both Bibles and UniSent wordlists. All models are trained to carry out 200 merges.
    - text_stats: All the intermediate files used to calculate the distribution-based metrics of morphological complexity over the subword-tokenized texts. Of particular interest might be the following files, which contain the final set of standardized distribution-based measures used as the character states in the Blomberg's _K_ analysis:
        - lang_vecs_standardized.tsv (for the statistics calculated over the parallel Bible corpora)
        - lang_vecs_unisent_standardized.tsv (for the statistics calculated over the UniSent word lists)
    - tokenized_corpora: the parallel Bibles and Unisent word lists after applying BPE tokenization to them. Also includes frequency lists of space-separated words and subwords. 
    - unisent_clean: The UniSent wordlists used following preprocessing (original versions downloaded from https://github.com/ehsanasgari/UniSent/tree/master)

-scripts


