import scipy
import numpy as np
import pandas as pd
from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.evaluation import precision_at_k, recall_at_k
from lightfm.cross_validation import random_train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from unidecode import unidecode # to deal with accents
from playground.datasources.datasource import DataSource
from playground.datasources.excel import ExcelDataSource

excel: DataSource = ExcelDataSource()
print(excel.get_students()["username"])

# books
# transactions
# studnets, cohort
# departments
