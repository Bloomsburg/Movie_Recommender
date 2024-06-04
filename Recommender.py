## Sean Bloomsburg
## sbloomsburg@gmail.com

import Customer
import Extrapolater
import Learning
import Vectorizer
from math import *
import re


def main():
    attribute_re = re.compile('\d+')
    threshold = 0.5

    ## Creates lists of moves with rating, genre, and title information
    ## to cross reference
    movie_info = Extrapolater.dbase_analysis()
    movie_rating_dictionary = movie_info[0]
    title_genre_dictionary = movie_info[1]
    movies = movie_rating_dictionary.keys()   

    ## Creates user item vector
    customer_item_vector = Customer.build_user_vector(movie_rating_dictionary, title_genre_dictionary)
    
    ## Learn to predict which movies a user will like
    user_weight_dictionary = Learning.learn(customer_item_vector, movie_rating_dictionary, title_genre_dictionary)
    
    ## Evaluation:
    ## Calculates the distance between the user's mean
    ## item vector and sample movies

    true_positive = 0.0
    false_negative = 0.0
    false_positive = 0.0
    true_negative = 0.0
    test_movie_list = open( "test.txt", "r")
    for movie in test_movie_list:
        user = attribute_re.search(movie).group()
        length = attribute_re.search(movie).span()
        movie = movie[length[1]:]

        current_movie = attribute_re.search(movie).group()
        length = attribute_re.search(movie).span()
        movie = movie[length[1]:]

        customer_rating = attribute_re.search(movie).group()
        length = attribute_re.search(movie).span()
        movie = movie[length[1]:]
        if current_movie in movie_rating_dictionary:
            rating = int(movie_rating_dictionary[current_movie])

            data = title_genre_dictionary[current_movie]
            rated_item_vector = []
            rated_item_vector.extend(data[1])
            rated_item_vector.append(rating)

            user_vector = []
            user_vector.extend(customer_item_vector[user])
            for i in range(20):
                user_vector[i] = user_vector[i] * user_weight_dictionary[user]

            ## Finds the distance between a user's
            ## mean item vector and an item
            hypothesis = Vectorizer.find_similarity(user_vector, rated_item_vector)

            if float(customer_rating) >= 3.0:
                if hypothesis <= threshold:
                    true_positive = true_positive + 1.0
                else:
                    false_negative = false_negative + 1.0
            if float(customer_rating) < 3.0:
                if hypothesis <= threshold:
                    false_positive = false_positive + 1.0
                else:
                    true_negative = true_negative + 1.0

    ## Results
    print "True Positive: ", true_positive
    print "False Positive: ", false_positive
    print "True Negative: ", true_negative
    print "False Negative: ", false_negative

    sensitivity = (true_positive / (true_positive + false_negative)) * 100.0
    sensitivity = str(sensitivity)
    missed_chances = (false_negative / (true_positive + false_negative)) * 100.0        
    missed_chances = str(missed_chances)

    print "sensitivity: " + sensitivity + "%"
    print "Missed Chances: ", false_negative
    print "Missed Chances Percent: " + missed_chances + "%"

main()
