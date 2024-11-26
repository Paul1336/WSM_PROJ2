echo "=============================stemming================================================="
echo "bm25 stemming result on 40 queries"
perl trec_eval.pl ../../data/qrels.401_440.txt ./bm25_stemming_40.run

echo "lmLaplace stemming result on 40 queries"
perl trec_eval.pl ../../data/qrels.401_440.txt ./lmLaplace_stemming_40.run

echo "lmJelinekMercer stemming result on 40 queries"
perl trec_eval.pl ../../data/qrels.401_440.txt ./lmJelinekMercer_stemming_40.run

echo "=============================no stemming================================================="

echo "bm25 no stemming result on 40 queries"
perl trec_eval.pl ../../data/qrels.401_440.txt ./bm25_nostemming_40.run

echo "lmLaplace no stemming result on 40 queries"
perl trec_eval.pl ../../data/qrels.401_440.txt ./lmLaplace_nostemming_40.run

echo "lmJelinekMercer no stemming result on 40 queries"
perl trec_eval.pl ../../data/qrels.401_440.txt ./lmJelinekMercer_nostemming_40.run

echo "=============================stemming(training set)================================================="

echo "bm25 stemming result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./bm25_stemming_10.run

echo "lmLaplace stemming result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./lmLaplace_stemming_10.run

echo "lmJelinekMercer stemming result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./lmJelinekMercer_stemming_10.run

echo "=============================Learning to Rank================================================="

echo "logistic_regression_full_weight_10 model result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./logistic_regression_full_weight_10.run

echo "logistic_regression_full_10 model result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./logistic_regression_full_10.run

echo "logistic_regression_partial_weight_10 model result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./logistic_regression_partial_weight_10.run

echo "logistic_regression_partial_10 model result on 10 queries"
perl trec_eval.pl ../../data/qrels.441_450.txt ./logistic_regression_partial_10.run