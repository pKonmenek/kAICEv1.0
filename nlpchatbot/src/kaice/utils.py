
from kaice.models import *
from kaice.settings import *
import codecs

def generate_corpus():
    messages = Message.select().where(
            Message.id.in_(Reply.select(Reply.received_id))
    )
    msg_texts = [msg.text+'\n' for msg in messages]
    corpus_file = codecs.open(CORPUS_PATH, 'w', 'utf-8')
    for msg_text in msg_texts:
        corpus_file.write(msg_text)
    corpus_file.close()
        
if __name__=='__main__':
    generate_corpus()