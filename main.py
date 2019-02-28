
class Photo:
    def __init__(self, id, tags, is_horizontal):
        self.id = id
        self.is_horizontal = is_horizontal
        self.tags = tags

def main(filename):
    photos = Parser.parseCollection()
    slides = create_slides_list(photos)
    
    
def create_slides_list(photos):
    slides = []
    passed_photos = []
    while(photos)
        cur_photo = photos.pop()
        if photo.is_horizontal:
            new_slide = Slide([photo.id], photo.is_horizontal, photo.tags)
        else:
            for second_photo in photos:
                if not photos.is_horisontal:
                    new tags = photo.tags | second_photo.tags
                    new_slide = Slide([photo.id, second_photo.id], photo.is_horizontal, tags)
        slides.append(new_slide)

