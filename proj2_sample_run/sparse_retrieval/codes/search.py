from pyserini.search.lucene import LuceneSearcher
from tqdm import tqdm
import os
from jnius import autoclass

DirectoryReader = autoclass('org.apache.lucene.index.DirectoryReader')
#FSDirectory = autoclass('org.apache.lucene.store.FSDirectory')
IndexSearcher = autoclass('org.apache.lucene.search.IndexSearcher')
Paths = autoclass('java.nio.file.Paths')
LMDirichletSimilarity = autoclass('org.apache.lucene.search.similarities.LMDirichletSimilarity')
LMJelinekMercerSimilarity = autoclass('org.apache.lucene.search.similarities.LMJelinekMercerSimilarity')




class CustomSearcher(LuceneSearcher):
    def set_bm25(self, k1=2, b=0.75):
        super().set_bm25(k1=k1, b=b)

    def set_Laplace(self):
        self.object.similarity = LMDirichletSimilarity()
        self.object.searcher = IndexSearcher(self.object.reader)
        self.object.searcher.setSimilarity(self.object.similarity)

    def set_JelinekMercer(self, lamda):
        self.object.similarity = LMJelinekMercerSimilarity(lamda)
        self.object.searcher = IndexSearcher(self.object.reader)
        self.object.searcher.setSimilarity(self.object.similarity)

def search(searcher, query, args):
    output = open(args.output, 'w')
        
    print(f'Do {args.method} search...')
    print(f'number of text: {searcher.num_docs}')
    for qid, qtext in tqdm(query.items()):
        #hits = searcher.search(qtext, args.k)
        hits = searcher.search(qtext, k=100000000)
        for i in range(len(hits)):
            # trec format: qid Q0 docid rank score method
            output.write(f'{qid} Q0 {hits[i].docid} {i+1} {hits[i].score:.5f} {args.method}\n')
