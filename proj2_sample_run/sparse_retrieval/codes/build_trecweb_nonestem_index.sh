python -m pyserini.index.lucene \
  --collection TrecwebCollection \
  --input ../data/WT2G \
  --index indexes/collection/noStemmer \
  --generator DefaultLuceneDocumentGenerator \
  --threads 6 \
  --stemmer none \
  --storePositions --storeDocvectors --storeRaw
