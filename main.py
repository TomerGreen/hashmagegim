

def main():



def create_slides_list(photos):
    slides = []
    for photo in photos:
        if photo.is_horizontal:
            new_slide = Slide([photo.id], photo.is_horizontal, photo.tags)
            slides.append()



