#./clean.sh


#############################################################################
# We first convert WT2G files into the jsonl format required by pyserini.   #
# No need this step when Using TrecwebCollection instead of JsonCollection. #
#############################################################################
# python codes/convert_wt2g_to_jsonl.py


##################################################################
# Secondly, we can build index for our WT2G corpus(247491 docs). #
# Use TrecwebCollection to build WT2G corpus(246772).            #
##################################################################
# ./codes/build_index.sh
#./codes/build_trecweb_index.sh
#./codes/build_trecweb_nonestem_index.sh


##########################################################
# Then, search and store result in the trec_eval format. #
##########################################################



##############################
# Lastly, do the evaluation. #
##############################


#python codes/main.py --query ../data/topics.401.txt --method bm25 --output runs/bm25_1.run --index indexes/collection/noStemmer
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401.txt runs/bm25_1.run

#python codes/main.py --query ../data/topics.401.txt --method lmLaplace --output runs/lmLaplace.run --index indexes/collection/noStemmer
#echo "lmLaplace result on 40 queries"
#perl trec_eval.pl ../data/qrels.401.txt runs/lmLaplace.run

#python codes/main.py --query ../data/topics.401.txt --method lmJelinekMercer --output runs/lmJelinekMercer.run --index indexes/collection/noStemmer
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401.txt runs/lmJelinekMercer.run

#python codes/main.py --query ../data/topics.401_410.txt --method bm25 --output runs/bm25.run --index indexes/collection/noStemmer
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401_410.txt runs/bm25.run

#python codes/main.py --query ../data/topics.401_410.txt --method lmLaplace --output runs/lmLaplace.run --index indexes/collection/noStemmer
#echo "lmLaplace result on 40 queries"
#perl trec_eval.pl ../data/qrels.401_410.txt runs/lmLaplace.run

#python codes/main.py --query ../data/topics.401_410.txt --method lmJelinekMercer --output runs/lmJelinekMercer.run --index indexes/collection/noStemmer
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401_410.txt runs/lmJelinekMercer.run

#stemmed
#echo "============================================================stemmed=========================================================================="

#python codes/main.py --query ../data/topics.401.txt --method bm25 --output runs/bm25_1.run --index indexes/collection/Stemmed
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401.txt runs/bm25_1.run

#python codes/main.py --query ../data/topics.401.txt --method lmLaplace --output runs/lmLaplace.run --index indexes/collection/Stemmed
#echo "lmLaplace result on 40 queries"
#perl trec_eval.pl ../data/qrels.401.txt runs/lmLaplace.run

#python codes/main.py --query ../data/topics.401.txt --method lmJelinekMercer --output runs/lmJelinekMercer.run --index indexes/collection/Stemmed
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401.txt runs/lmJelinekMercer.run

#python codes/main.py --query ../data/topics.401_410.txt --method bm25 --output runs/bm25_1.run --index indexes/collection/Stemmed
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401_410.txt runs/bm25_1.run

#python codes/main.py --query ../data/topics.401_410.txt --method lmLaplace --output runs/lmLaplace.run --index indexes/collection/Stemmed
#echo "lmLaplace result on 40 queries"
#perl trec_eval.pl ../data/qrels.401_410.txt runs/lmLaplace.run

#python codes/main.py --query ../data/topics.401_410.txt --method lmJelinekMercer --output runs/lmJelinekMercer_2.run --index indexes/collection/Stemmed
#echo "BM25 result on 40 queries"
#perl trec_eval.pl ../data/qrels.401_410.txt runs/lmJelinekMercer_2.run

#python codes/main.py --query ../data/topics.441_450.txt --method bm25 --output runs/bm25_stemmed_testset.run --index indexes/collection/Stemmed
#echo "BM25 result on 10 queries"
#perl trec_eval.pl ../data/qrels.441_450.txt runs/bm25_stemmed_testset.run

#python codes/main.py --query ../data/topics.441_450.txt --method lmLaplace --output runs/lmLaplace_stemmed_testset.run --index indexes/collection/Stemmed
#echo "lmLaplace result on 10 queries"
#perl trec_eval.pl ../data/qrels.441_450.txt runs/lmLaplace_stemmed_testset.run

#python codes/main.py --query ../data/topics.441_450.txt --method lmJelinekMercer --output runs/lmJelinekMercer_stemmed_testset.run --index indexes/collection/Stemmed
#echo "lmJelinekMercer result on 10 queries"
perl trec_eval.pl ../data/qrels.441_450.txt runs/formatted_predictions2.run
