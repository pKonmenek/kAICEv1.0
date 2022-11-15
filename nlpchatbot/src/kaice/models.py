from email.policy import default
from peewee import *
from datetime import datetime
from kaice.settings import DATABASE_FILE
db = SqliteDatabase(DATABASE_FILE)

def create_tables():
    with db:
        db.create_tables([Message, Reply, BotMemory, Conversation])
        


class BaseModel(Model):
    class Meta:
        database = db

class Message(BaseModel):
    text = CharField(unique=True)
    
    
    
class Reply(BaseModel):
    received = ForeignKeyField(Message)
    replied = ForeignKeyField(Message)

class BotMemory(BaseModel):
    bot_name = CharField(unique=True)

class Conversation(BaseModel):
    name = CharField(unique=True)
    last_msg_time = DateTimeField(default=datetime.now())
    last_replied_msg = CharField(unique=False)
    msg_nbr = IntegerField(default=0)
    bot = ForeignKeyField(BotMemory)

class User(BaseModel):
    username = CharField(unique = True)
    password = CharField(max_length=255)

    
create_tables()