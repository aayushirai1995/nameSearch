from trie import Trie
from operator import itemgetter


def getindexMap(data):
    indexMap = {}

    for row in data:
        for term in row:
            if term not in indexMap:
                indexMap[term] = [" ".join(" ".join(row).split())]
            else:
                indexMap[term].append(" ".join(" ".join(row).split()))

    return indexMap


def readFileToLines(filepath):
    with open(filepath, encoding="utf8") as f:
        content = f.readlines()
    content = [x[:-1].lower() for x in content]
    return content


def searchQuery(query, trie, indexMap):
    results = []
    for leafNode in trie.start_with_prefix(query):
        results.extend(indexMap[leafNode])

    results = list(set(results))

    scoreMap = {}
    for result in results:
        score = 0
        token = result.split()

        if token[0] == query:
            score = 200
        elif token[0].startswith(query):
            score = 30

        if len(token) == 2:
            if token[1] == query:
                score += 100
            elif token[1].startswith(query):
                score += 20

        if len(token) == 3:
            if token[2] == query:
                score += 100
            elif token[2].startswith(query):
                score += 20
            elif token[1] == query:
                score += 50
            elif token[1].startswith(query):
                score += 10

        scoreMap[result] = score

    scoreMap = dict(sorted(scoreMap.items(), key=itemgetter(1), reverse=True))
    return scoreMap.keys()