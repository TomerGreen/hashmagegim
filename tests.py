from parser import *
from main import *

def testCollectionParser(filename):
    collection = parseCollection(filename)
    for photo in collection:
        print(str(photo.id) + ' ' + str(photo.isHorizontal) + ' ' + str(photo.tags))


if __name__ == '__main__':
    testCollectionParser('a_example.txt')