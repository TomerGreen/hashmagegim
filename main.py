import parser
import numpy as np

class Photo:
    def __init__(self, id, is_horizontal, tags):
        self.id = id
        self.is_horizontal = is_horizontal
        self.tags = tags

class Slide:
    def __init__(self, id, photo_ids, is_horizontal, tags):
        self.id = id
        self.photo_ids = photo_ids
        self.is_horizontal = is_horizontal
        self.tags = tags


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

def output_parser(slides):
    file = open("sub_b_lovely_landscapes.txt", 'w')
    file.write("%d\n" % len(slides))
    for slide in slides:
        if len(slide.photo_ids) == 1:
            file.write("%d" % slide.photo_ids[0])
        else:
            file.write("%d " % slide.photo_ids[0])
            file.write("%d" % slide.photo_ids[1])
        file.write("\n")

def score_slides(s1, s2):
    inter = s1.tags.intersection(s2.tags)
    sub1 = s1.tags.difference(s2.tags)
    sub2 = s2.tags.difference(s1.tags)
    return min(len(inter), len(sub1), len(sub2))

def intersection_lists(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def slides_scores(slides):
    score_mat = np.zeros((len(slides), len(slides)))
    scores = {}
    for slide1 in slides:
        for slide2 in slides:
            if slide1 is slide2:
                scores[(slide1, slide2)] = -1
                score_mat[slide1.id, slide2.id] = -1
            elif len(intersection_lists(slide1.photo_ids, slide2.photo_ids)) > 0:
                score_mat[slide1.id, slide2.id] = -1
            else:
                scores[(slide1, slide2)] = score_slides(slide1, slide2)
                score_mat[slide1.id, slide2.id] = score_slides(slide1, slide2)
    return score_mat


def main(filename):
    photos = parseCollection(filename)
    # slides = create_slides_list(photos)
    # score_mat = slides_scores(slides)
    path = run_DFS(slides, score_mat, 1)
    print(path)
    slides_output_list = []
    for id in path:
        slides_output_list.append(slides[id])
    output_parser(slides_output_list)

def DFS(slides, score_map_copy, cur_slide, path, path_score, limit):
    path.append(cur_slide)
    for i in range(limit):
        # score_map_copy = np.copy(score_map)
        max_index = np.argmax(score_map_copy[cur_slide])
        if score_map_copy[cur_slide, max_index] < 0:
            return path, path_score
        path_score += score_map_copy[cur_slide, max_index]
        score_map_copy[cur_slide] = -1
        score_map_copy[:, cur_slide] = -1
        return DFS(slides, score_map_copy, max_index, path, path_score, limit)



def run_DFS(slides, score_mat, limit):
    max_path, max_path_score = [], 0
    for cur_slide in slides:
        path = []
        score_map_copy = np.copy(score_mat)
        new_path, new_path_score = DFS(slides, score_map_copy, cur_slide.id, path, 0, limit)
        if max_path_score < new_path_score:
            max_path_score = new_path_score
            max_path = new_path
    return max_path


def create_slides_list(photos_arg):
    photos = photos_arg
    slides = []
    while(photos):
        cur_photo = photos.pop()
        if cur_photo.is_horizontal:
            new_slide = Slide(len(slides), [cur_photo.id], cur_photo.is_horizontal, cur_photo.tags)
            slides.append(new_slide)
        else:
            for second_photo in photos:
                if not second_photo.is_horizontal:
                    new_tags = cur_photo.tags | second_photo.tags
                    new_slide = Slide(len(slides), [cur_photo.id, second_photo.id], cur_photo.is_horizontal, new_tags)
                    slides.append(new_slide)
    return slides

if __name__ == '__main__':
    main("b_lovely_landscapes.txt")