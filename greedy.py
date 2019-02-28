def score_slides(s1, s2):
    inter = s1.intersection(s2)
    sub1 = s1.difference(s2)
    sub2 = s2.difference(s1)
    return min(len(inter), len(sub1), len(sub2))


def slides_scores(slides):
    scores = {}
    for slide1 in slides:
        for slide2 in slides:
            if slide1 is slide2:
                scores[(slide1, slide2)] = -1
            else:
                scores[(slide1, slide2)] = score_slides(slide1, slide2)
    return scores

