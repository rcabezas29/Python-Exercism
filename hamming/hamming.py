def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("value error")
    ret = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            ret += 1
    return ret
