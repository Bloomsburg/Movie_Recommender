## Sean Bloomsburg
## sbloomsburg@gmail.com
##
## This module uses the similarity function to learn
## a weight value that will be used according to the
## second function outlined in the Movie Recommender Explanation.
##
import Vectorizer
from math import *
import re

def learn(user_item_vector, movie_rating_dictionary, title_genre_dictionary):
    attribute_re = re.compile('\d+')
    user_weight_dictionary = {}

    keys = user_item_vector.keys()
    for key in keys:
        current_user = key
        weight = 1.0
        Last_weight = 0.0
        e_theta = 77.0
        last_e_theta = 88.0

        while e_theta < last_e_theta :
            training_data = open( "learn.txt", "r")
            rated_item_vector = []
            hypothesis = 0

            weight = weight + 0.01

            for line in training_data:
                item = line

                user = attribute_re.search(item).group()
                length = attribute_re.search(item).span()
                item = item[length[1]:]

                if user == current_user:

                    current_movie = attribute_re.search(item).group()
                    length = attribute_re.search(item).span()
                    item = item[length[1]:]

                    user_rating = attribute_re.search(item).group()
                    length = attribute_re.search(item).span()
                    item = item[length[1]:]

                    if float(user_rating) >= 3.0:

                        rating = int(movie_rating_dictionary[current_movie])
                        movie_data = title_genre_dictionary[current_movie]
                        rated_item_vector = []
                        rated_item_vector.extend(movie_data[1])
                        rated_item_vector.append(rating)

                        user_vector = []
                        user_vector.extend(user_item_vector[user])
                        for i in range(20):
                            user_vector[i] = user_vector[i] * weight

                        hx = Vectorizer.find_similarity(user_vector, rated_item_vector)
                        hypothesis = hypothesis + abs(hx - 1.0)**2

                    if float(user_rating) < 3.0:
                        rating = float(movie_rating_dictionary[current_movie])
                        movie_data = title_genre_dictionary[current_movie]
                        rated_item_vector = []
                        rated_item_vector.extend(movie_data[1])
                        rated_item_vector.append(rating)
                        user_vector = user_item_vector[user]

                        for i in range(20):
                            user_vector[i] = user_vector[i] * weight

                        hx = Vectorizer.find_similarity(user_vector, rated_item_vector)
                        hypothesis = hypothesis + abs(hx - 0.0)**2

            last_e_theta = e_theta
            e_theta = hypothesis / 2.0
            user_weight_dictionary[current_user] = weight

    return user_weight_dictionary
if __name__ == learn:
    learn
