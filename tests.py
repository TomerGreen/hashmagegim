from parser import *
from main import *
from slides_extractor import *
from salesman_sol import *

def testCollectionParser(filename):
    collection = parseCollection(filename)
    for photo in collection:
        print(str(photo.id) + ' ' + str(photo.isHorizontal) + ' ' + str(photo.tags))


def testSalesman(filename):
    print("1")
    slides = get_slides(filename)
    slides = get_route(slides)
    for slide in slides:
        print(slide.photo_ids)


if __name__ == '__main__':
    testSalesman('a_example.txt')