import os

print("basename: ", os.path.basename(__file__))
print("dirname: ", os.path.dirname(os.path.abspath(__file__)))
fullpath = os.path.dirname(os.path.abspath(__file__))
print(fullpath)
fp = os.path.abspath(fullpath+os.sep+'../datasources/corpus.txt')
print(fp)