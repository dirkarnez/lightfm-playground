import numpy as np

from lightfm.datasets import fetch_movielens

data = fetch_movielens(min_rating=5.0)

print("hello")