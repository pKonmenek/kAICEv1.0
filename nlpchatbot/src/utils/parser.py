import json
import csv
from models import Message, Reply
    
def parse_json_to_csv(filename):
    csv_output = filename.replace('json', 'csv')
    csv_file = open(csv_output, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["Question", "Reponse"])    
    with open(filename, 'r') as f:
        jdata = json.load(f)
        data = jdata.get('data')
        for d in data:
            for p in d['paragraphs']:
                for qa in p['qas']:
                    q = qa['question']
                    response = ""
                    for rep in qa['answers']:
                        if len(response) > 0:
                            response+="."
                        response+=rep['text']
                    writer.writerow([q, response])
    csv_file.close()
    

def csv_to_sqlite(filename):
    with open(filename, 'r', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f)
        # reader = [r for r in reader]
        for row in reader:
            print("ENREGISTREMENT EN BD: ", row[1], row[0])
            msg = Message.get_or_create(text=row[0])
            if msg[1]:
                msg[0].save()
            rep = Message.get_or_create(text=row[1])
            if rep[1]:
                rep[0].save()
            qr = Reply.get_or_create(received=msg[0], replied=rep[0])
            if qr[1]:
                qr[0].save()
    
    
if __name__=="__main__":
    # parse_json_to_csv("piafV1.0.json")
    csv_to_sqlite('train.csv')
            
    
