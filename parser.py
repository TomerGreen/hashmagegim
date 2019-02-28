from main import *


def parsePhoto(photoline, id):
    linelist = photoline.split()
    isHorizontal = False
    if linelist[0] == 'H':
        isHorizontal = True
    tags = set(linelist[2:])
    return Photo(id, isHorizontal, tags)


def parseCollection(filename):
    with open(filename) as f:
        lines = f.readlines()[1:]
        lines = [x.strip() for x in lines]  # removes newline chars.
    photoCount = 0
    collection = list()
    for line in lines:
        collection.append(parsePhoto(line, photoCount))
        photoCount += 1
    return collection
