from main import *
from parser import *
from greedy import *
import tsp


def create_distance_matrix(slides):
    mat = list()
    for s1 in slides:
        temp_list = list()
        for s2 in slides:
            temp_list.append(score_slides(s1.tags, s2.tags))
        mat.append(temp_list)
    return mat


def get_route(slides):
    mat = create_distance_matrix(slides)
    r = range(len(mat))
    dist = {(i, j): mat[i][j] for i in r for j in r}
    sol = tsp.tsp(r, dist)[1]
    min_score = 999999999999999999
    cut_after_index = 0
    for index in sol:
        tags1 = slides[index].tags
        if index == len(slides) - 1:
            tags2 = slides[0].tags
        else:
            tags2 = slides[index+1].tags
        score = score_slides(tags1, tags2)
        if score < min_score:
            min_score = score
            cut_after_index = index
    perm_sol = sol[cut_after_index:] + sol[0:cut_after_index]
    if cut_after_index == len(slides) - 1:
        perm_sol = sol
    ordered_slides = list()
    for index in perm_sol:
        ordered_slides.append(slides[index])
    return ordered_slides
