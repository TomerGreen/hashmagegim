def score_slides(s1, s2):
    inter = s1.intersection(s2)
    sub1 = s1.difference(s2)
    sub2 = s2.difference(s1)
    return min(len(inter), len(sub1), len(sub2))

