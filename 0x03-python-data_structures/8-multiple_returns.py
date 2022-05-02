#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()

    if(len(sentence) == 0):
        new_tuple += (0,)
        new_tuple += (None,)
    else:
        new_tuple += (len(sentence),)
        new_tuple += (sentence[0],)
    return(new_tuple)
