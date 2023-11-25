from random import shuffle

def make_shuffled_list(size):

    shuffled_list = []
    for i in range(size):
        shuffled_list.append(i)
    shuffle(shuffled_list)
    return shuffled_list