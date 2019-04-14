from flask import Flask
from flask import request
from search import *
import time

app = Flask(__name__)
cache = {}


def prepareData():
    # reading data fileC:\Users\611285957\Downloads
    path = "data.csv"
    content = readFileToLines(path)
    content = content[1:]

    # cleaning data
    data = []
    for row in content:
        tokens = row.split(",")
        if len(tokens) == 3 and not (tokens[0] == "" and tokens[1] == "" and tokens[2] == ""):
            data.append(tokens)

    # get uniqueTerms
    uniqueTerms = set()
    for row in data:
        for term in row:
            uniqueTerms.add(term)

    # trie data stuctures to store uniqueTerms
    trie = Trie()
    for term in uniqueTerms:
        trie.add(term)

    cache['trie'] = trie
    cache['indexMap'] = getindexMap(data)


@app.route('/search')
def search():
    startTime = time.time()

    if 'indexMap' not in cache or 'trie' not in cache:
        print("Loading cache")
        prepareData()
    else:
        print("request being served from exiting cache")

    trie = cache['trie']
    indexMap = cache['indexMap']

    result = str(list(searchQuery(request.args['query'].lower(), trie, indexMap)))

    print("Time taken for request: " + str(1000 * (time.time() - startTime)) + "ms")

    return result


if __name__ == '__main__':
    app.run()