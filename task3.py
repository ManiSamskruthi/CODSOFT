import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5],
    'movie_id': ['A', 'B', 'C', 'A', 'B', 'B', 'C', 'A', 'C', 'B'],
    'rating': [5, 3, 4, 4, 5, 4, 2, 5, 3, 4]
}
ratings_df = pd.DataFrame(data)
user_movie_matrix = ratings_df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
def get_recommendations(user_id, user_movie_matrix, user_similarity_df):
    sim_scores = user_similarity_df[user_id]
    weighted_ratings = user_movie_matrix.T.dot(sim_scores)
    user_rated_movies = user_movie_matrix.loc[user_id][user_movie_matrix.loc[user_id] > 0].index
    recommendations = weighted_ratings[~weighted_ratings.index.isin(user_rated_movies)]
    return recommendations.sort_values(ascending=False).head(5)
recommended_movies = get_recommendations(user_id=1, user_movie_matrix=user_movie_matrix, user_similarity_df=user_similarity_df)
print("Recommended movies for User 1:")
print(recommended_movies)
