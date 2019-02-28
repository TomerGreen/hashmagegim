import numpy as np
def score_slides(s1, s2):
    inter = s1.intersection(s2)
    sub1 = s1.difference(s2)
    sub2 = s2.difference(s1)
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
                score_mat[slide1.id][slide2.id] = -1
            elif len(intersection_lists(slide1.photo_ids, slide2.photo_ids)) > 0:
                score_mat[slide1.id][slide2.id] = -1
            else:
                scores[(slide1, slide2)] = score_slides(slide1, slide2)
                score_mat[slide1.id][slide2.id] = score_slides(slide1, slide2)
    return score_mat

