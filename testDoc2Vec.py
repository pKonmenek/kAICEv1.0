import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os
import gensim
import csv
# Set file names for train and test data
#test_data_dir = os.path.join(gensim.__path__[0], 'test', 'test_data')

train_file = r"nlpchatbot\src\train.csv"
test_file = r"nlpchatbot\src\valid.csv"

import smart_open
import pandas as pd

#def read_corpus(fname, tokens_only=False):
    #file = pd.read_csv(fname)
    #file[0].values



def read_corpus(fname, tokens_only=False):
   with smart_open.open(fname, encoding="utf-8") as f:
       r = csv.reader(f, delimiter=',')
       for i, line in  r:
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

train_corpus = list(read_corpus(train_file))
test_corpus = list(read_corpus(test_file, tokens_only=True))

print(train_corpus[:2])
print('\n\n')
print(test_corpus[:2])

model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)

print('\n\n')

model.build_vocab(train_corpus)

print(f"Le mot 'astéroïde' apparait {model.wv.get_vecattr('astéroïde', 'count')} fois dans le corpus d'entrainement.")

print('\n\n')

model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

print('\n\n')

vector = model.infer_vector(['Quelles', 'fleurs', 'aident', 'à', 'la', 'digestion'])
print(vector)

print('\n\n')

print(len(train_corpus))
print(train_corpus[1].words)


ranks = []
second_ranks = []
for doc_id in range(len(train_corpus)):
    inferred_vector = model.infer_vector(train_corpus[doc_id].words)
    sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)

    second_ranks.append(sims[1])

print('\n\n')

import collections

counter = collections.Counter(ranks)
print(counter)

print('\n\n')

print('Document ({}): «{}»\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('SECOND-MOST', 1), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))


print('\n\n')

# Pick a random document from the corpus and infer a vector from the model
import random
doc_id = random.randint(0, len(train_corpus) - 1)

# Compare and print the second-most-similar document
print('Train Document ({}): «{}»\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
sim_id = second_ranks[doc_id]

print('####################################\n')

print('Similar Document {}: «{}»\n'.format(sim_id, ' '.join(train_corpus[sim_id[0]].words)))

print('\n\n')

# Pick a random document from the test corpus and infer a vector from the model
doc_id = random.randint(0, len(test_corpus) - 1)
inferred_vector = model.infer_vector(test_corpus[doc_id])
sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))

# Compare and print the most/median/least similar documents from the train corpus
print('Test Document ({}): «{}»\n'.format(doc_id, ' '.join(test_corpus[doc_id])))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))