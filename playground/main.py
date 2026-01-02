from typing import Any, List

import numpy as np
from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k
from playground.generators.generators import StudentsGenerator


StudentsGenerator().generate_students()
# Load the MovieLens 100k dataset. Only five
# star ratings are treated as positive.
movielens_data = fetch_movielens(min_rating=5.0)
# movielens_data['item_labels']

# for key, value in movielens_data.items():
#     print(key, type(value), value.shape)

# Instantiate and train the model
model = LightFM(loss='warp')
model.fit(movielens_data['train'], epochs=30, num_threads=2)

# Evaluate the trained model
print("Train precision: %.2f" % precision_at_k(model, movielens_data['train'], k=5).mean())
print("Test precision: %.2f" % precision_at_k(model, movielens_data['test'], k=5).mean())

def sample_recommendation(model: LightFM, movielens_data: dict[str, Any], user_ids: List[int]):
    n_users, n_items = movielens_data['train'].shape

    for user_id in user_ids:
        known_positives = movielens_data['item_labels'][movielens_data['train'].tocsr()[user_id].indices]
        
        scores = model.predict(user_id, np.arange(n_items))
        top_items = movielens_data['item_labels'][np.argsort(-scores)]
        
        print("User %s" % user_id)
        print("     Known positives:")
        
        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")
        
        for x in top_items[:3]:
            print("        %s" % x)
        
sample_recommendation(model, movielens_data, [3, 25, 450]) 
