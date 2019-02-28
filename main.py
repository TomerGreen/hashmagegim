import parser
class Photo:
    def __init__(self, id, tags, is_horizontal):
        self.id = id
        self.is_horizontal = is_horizontal
        self.tags = tags

def main(filename):
    photos = parser.parseCollection(filename)
    slides = create_slides_list(photos)
    
    
def create_slides_list(photos):
    slides = []
    passed_photos = []
    while(photos):
        cur_photo = photos.pop()
        if cur_photo.is_horizontal:
            new_slide = Slide([cur_photo.id], cur_photo.is_horizontal, cur_photo.tags)
            slides.append(new_slide)
        else:
            for second_photo in photos:
                if not second_photo.is_horisontal:
                    new_tags = cur_photo.tags | second_photo.tags
                    new_slide = Slide([cur_photo.id, second_photo.id], cur_photo.is_horizontal, new_tags)
                    slides.append(new_slide)

