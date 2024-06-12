from itertools import product

combs = map(
    lambda tup: b"".join([bytes(x) for x in tup]), product(range(128), repeat=2)
)
