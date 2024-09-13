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

- scripts
    - rmd_html: contains versions of the R-markdown files in HTML so the output can be seen along with the code. The corresponding .rmd files are in the ./scripts directory
        - figure.html: code to generate language sample map
        - phylosig_bpe.html: Code for Blomberg's _K_ analysis with phytools (for both Bible analyses and the UniSent experiment)
        - picante.html: Code for the Blomberg's _K_ analysis using picante
    - All other scripts in this directory are bash and python scripts used to preprocess data, train and apply BPE models, and calculate the relevant distribution-based metrics. Some scripts for calculating the metrics over subword vocabularies are adapted from the publicly available GitHub repositories by Gutierrez-Vasques et al. 2021 and 2023 (https://github.com/ximenina/theturningpoint and [https://github.com/ximenina/theturningpoint](https://github.com/ximenina/BPEProductivity))
        - When a script is adapted from either of those repositories, it is noted within the script. 

References:

Ehsaneddin Asgari et al. “UniSent: Universal Adaptable Sentiment Lexica for 1000+
Languages”. In: Proceedings of the International Conference on Language Resources and
Evaluation (LREC-2020). European Language Resources Association (ELRA). 2020.

Will Chang et al. “Ancestry-constrained phylogenetic analysis supports the Indo-
European steppe hypothesis”. In: Language (2015), pp. 194–244.

Christos Christodouloupoulos and Mark Steedman. “A massively parallel corpus: the
bible in 100 languages”. In: Language resources and evaluation 49 (2015), pp. 375–395.

Ximena Gutierrez-Vasques, Christian Bentz, and Tanja Samardˇzi´c. “Languages through
the looking glass of bpe compression”. In: Computational Linguistics 49.4 (2023), pp. 943–
1001.

Ximena Gutierrez-Vasques, Christian Bentz, Olga Sozinova, et al. “From characters to
words: the turning point of BPE merges”. In: Proceedings of the 16th Conference of the
European Chapter of the Association for Computational Linguistics: Main Volume. 2021,
pp. 3454–3468.
