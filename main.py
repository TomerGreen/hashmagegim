
class Photo:
    def __init__(self, id, isHorizontal, tags):
        self.id = id
        self.isHorizontal = isHorizontal
        self.tags = tags

class Slide:
    def __init__(self, ids, isHorizontal, tags):
        self.ids = ids
        self.isHorizontal = isHorizontal
        self.tags = tags


def main():

def create_slides_list(photos):
    slides = []
    for photo in photos:
        if photo.is_horizontal:
            new_slide = Slide([photo.id], photo.is_horizontal, photo.tags)
            slides.append()
