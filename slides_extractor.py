from main import *
from parser import *
from greedy import *
from random import choice


def random_heuristic_vertical_pairing(vert_photos):
    slides = list()
    while len(vert_photos) >= 2:
        p1 = choice(vert_photos)
        min_score = 9999999999999999
        p2 = None
        for photo in vert_photos:
            if photo.id == p1.id:
                continue
            score = score_slides(photo.tags, p1.tags)
            if score < min_score:
                p2 = photo
                min_score = score
        slide = Slide(p1.id*10 + p2.id, [p1.id, p2.id], False, p1.tags.union(p2.tags))
        slides.append(slide)
        vert_photos = list(set(vert_photos).difference(set([p1, p2])))
    return slides


def get_slides(filename):
    slides = list()
    collection = parseCollection(filename)
    vert_photos = list()
    for photo in collection:
        if photo.is_horizontal:
            slides.append(Slide(photo.id, [photo.id], True, photo.tags))
        else:
            vert_photos.append(photo)
    vert_slides = random_heuristic_vertical_pairing(vert_photos)
    return slides + vert_slides

