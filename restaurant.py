# Simple Recommender System

import pandas as pd

rest_data = pd.read_csv("NARestaurants.csv")
print(rest_data.head())

"""
Weighted Rating -

(v/v+m) * R + (m/v+m) * C

v is the number of votes (vote count)
m is the minimum votes required to be listed in chart
R is the average rating for the movie (vote_average)
C is the mean vote across the whole report
"""

C = rest_data["weighted_rating_value"].mean()
print(C)

m = rest_data["aggregated_rating_count"].quantile(0.90)
print(m)

# Filter out all the qualified movies into a new DataFrame

q_rest = rest_data.copy().loc[rest_data["aggregated_rating_count"] >= m]
print(q_rest.shape)

def weighted_rating(x, m = m, C = C):
    v = x["aggregated_rating_count"]
    R = x["weighted_rating_value"]

    return (v/(v+m)*R) + (m/(m+v)*C)

q_rest["score"] = q_rest.apply(weighted_rating, axis = 1)
q_rest = q_rest.sort_values('score', ascending = False)
# Filter out all the qualified movies into a new DataFrame

q_rest = rest_data.copy().loc[rest_data["aggregated_rating_count"] >= m]
print(q_rest.shape)

def weighted_rating(x, m=m, C=C):
    v = x["aggregated_rating_count"]
    R = x["weighted_rating_value"]

    return (v/(v+m) * R) + (m/(m+v) * C)

q_rest["score"] = q_rest.apply(weighted_rating, axis=1)
q_rest = q_rest.sort_values('score', ascending=False)

# Filter out all the qualified movies into a new DataFrame

q_rest = rest_data.copy().loc[rest_data["aggregated_rating_count"] >= m]
print(q_rest.shape)

def weighted_rating(x, m = m, C = C):
    v = x["aggregated_rating_count"]
    R = x["weighted_rating_value"]

    return (v/(v+m)*R) + (m/(m+v)*C)

q_rest["score"] = q_rest.apply(weighted_rating, axis = 1)
q_movies = q_rest.sort_values('score', ascending = False)

# Filter out all the qualified movies into a new DataFrame
q_rest = rest_data.copy().loc[rest_data["aggregated_rating_count"] >= m]
print(q_movies.shape)

def weighted_rating(x, m=m, C=C):
    v = x["aggregated_rating_count"]
    R = x["weighted_rating_value"]

    return (v/(v+m) * R) + (m/(m+v) * C)

q_rest["score"] = q_rest.apply(weighted_rating, axis=1)
q_rest = q_rest.sort_values('score', ascending=False)

# Printing the Top 20 movies
print(q_rest[["name", "city", "aggregated_rating_count", "weighted_rating_value", "score"]].head(20))
