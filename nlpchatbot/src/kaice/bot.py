from random import randint
from gensim import corpora, models, similarities
from gensim.utils import simple_preprocess
import pickle
from loguru import logger
from kaice.settings import *
from kaice.models import *
# from settings import *
# from models import *



#corpus = [simple_preprocess(line) for line in open(CORPUS_PATH, encoding='utf-8')] 
#dictionary = corpora.Dictionary(corpus)
#BoW_corpus = [dictionary.doc2bow(text, allow_update=True) for text in corpus]
#tfidf = models.TfidfModel(BoW_corpus)


#In the example below, we are going to initialise the tf-idf model.
# We will train it on our corpus and then transform the string “trees graph”. 
#words = "Comment tu".lower().split()
#print(tfidf[dictionary.doc2bow(words)])

#index = similarities.SparseMatrixSimilarity(tfidf[BoW_corpus], num_features=len(dictionary))
#query_document = 'Comment tu'.split()
#query_bow = dictionary.doc2bow(query_document)
#simils = index[tfidf[query_bow]]
#decroissant = [(doc_number, score) for doc_number, score in sorted(enumerate(simils), key=lambda x: x[1], reverse=True)]
#print(decroissant)


class BotAI:
    
    def __init__(self):
        logger.info("BotAI starting...")
        self.text_corpus = None
        self.corpus = None
        self.dictionary = None
        self.bow_corpus = None
        self.tfidf = None
        self._load_files()
        self.index = similarities.SparseMatrixSimilarity(
            self.tfidf[self.bow_corpus], num_features=len(self.dictionary))
        logger.info("Datas loaded succesfully, ready for queries")
        
    
    def train(self):
        pass
    
    def replyto(self, msg:str) -> str:
        # On transforme le message recu en `document` puis en `bow`
        query_document = msg.split()
        query_bow = self.dictionary.doc2bow(query_document)
        # On cherche les indices des messages les plus similaires et on range par ordre de
        # similarites decroissantes
        simils = self.index[self.tfidf[query_bow]]
        dec = [(doc_number, score) for doc_number, 
                       score in sorted(enumerate(simils), key=lambda x: x[1], reverse=True)]
        res = None
        if dec:
            idx = dec[0][0]
            i, line = -1, ""
            # On parcours le fichier des corpus pour  trouver le message
            # corespondant a l'indice
            with open(CORPUS_PATH, 'r', encoding='utf-8') as f:
                while i != idx:
                    i, line = i+1, next(f)
            try:
                res = self.get_reply_to_message(line.strip())
                if not res:
                    self.learn_message(msg)
            except Exception as e:
                logger.exception(str(e))
        return res


    def learn_message(self, msg):
        msg = Message.get_or_create(text=msg)
        if msg[1]:
            msg[0].save()
            logger.info("Apprentissage d'un nouveau message: {}".format(msg[0]))

    def get_reply_to_message(self, msg)->str:
        """Trouve la reponse a un message dans la base de donnee.
        """
        res = ""
        try:
            m = Message.get_or_none(Message.text==msg)
            replies = []
            if m:
                replies = Reply.select().where(Reply.received_id == m.id)
            if replies:
                i = randint(0, len(replies)-1)
                res = replies[i].replied.text
        except Exception as e:
            logger.exception(str(e))
        return res

            
    
    def _load_files(self):
        try:
            self.corpus = [simple_preprocess(line) for line in open(
                CORPUS_PATH, encoding='utf-8')]
        except FileNotFoundError:
            logger.critical("Corpus file is missing. "
                            "It could be generated with `utils.utils.generate_corpus`")
        finally:
            try:
                self.dictionary = corpora.Dictionary.load(DICTIONARY_PATH)
            except FileNotFoundError:
                self.dictionary = corpora.Dictionary(self.corpus)
            try:
                self.bow_corpus = corpora.Dictionary.load(BOW_CORPUS_PATH)
            except FileNotFoundError:
                self.bow_corpus = [self.dictionary.doc2bow(
                    text, allow_update=True) for text in self.corpus]
            try:
                self.tfidf = corpora.Dictionary.load(TFIDF_PAHT)
            except FileNotFoundError:
                self.tfidf = models.TfidfModel(self.bow_corpus) 
            #except Exception as e:
                #logger.critical("Error while trying to open files: {}".format(e))                
    
    def _save_files(self):
        try:
            self.dictionary.save(DICTIONARY_PATH)
            self.tfidf.save(TFIDF_PAHT)
            with open(BOW_CORPUS_PATH, 'wb') as f:
                pickle.dump(self.tfidf, f)
        except Exception as e:
            logger.exception("Error while trying to dump datas to files: {}".fortat(e))


    def generate_corpus():
        messages = Message.select().where(
                Message.id.in_(Reply.select(Reply.received_id))
        )
        msg_texts = [msg.text+'\n' for msg in messages]
        corpus_file = codecs.open(CORPUS_PATH, 'w', 'utf-8')
        for msg_text in msg_texts:
            corpus_file.write(msg_text)
        corpus_file.close()
            
    def quit(self):
        self._save_files()
        logger.info("It was a pleasure to serve you. Bye")