#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_value = 0
    name_of_winner = ""
    if(a_dictionary is None):
        return None
    for player in a_dictionary:
        if(a_dictionary[player] > biggest_value):
            biggest_value = a_dictionary[player]
            name_of_winner = player
    if(biggest_value == 0):
        return(None)
    return(name_of_winner)
