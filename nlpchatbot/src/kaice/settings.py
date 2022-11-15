from os import path
import os

fullpath = os.path.dirname(os.path.abspath(__file__))
CORPUS_PATH = path.abspath(fullpath+os.sep+'../datasources/corpus.txt')
BOW_CORPUS_PATH = path.abspath(fullpath+os.sep+'../datasources/bow_corpus.p')
DICTIONARY_PATH = path.abspath(fullpath+os.sep+'../datasources/dic.p')
TFIDF_PAHT = path.abspath(fullpath+os.sep+'../datasources/tfidf.p')
WEBDRIVER_DIR = path.abspath(fullpath+os.sep+'../webdrivers')
WEBDRIVER_PATH = path.abspath(fullpath+os.sep+'../webdrivers/chromedriver.exe')
COOKIES_FILE_PATH = path.abspath(fullpath+os.sep+'../webdrivers/cookies.pkl')
ASSETS_DIR = path.abspath(fullpath+os.sep+'../gui/assets')
CSS_DIR = ASSETS_DIR + os.sep + 'css'
IMAGE_DIR = ASSETS_DIR + os.sep + 'images'
WEBDRIVER_DATA_DIR = WEBDRIVER_DIR + os.sep + 'data'
DATABASE_FILE = path.abspath(fullpath+os.sep+'../database/messages.db')
