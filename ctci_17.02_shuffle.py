Write a method to shuffle a deck of cards. 
It must be a perfect shuffle-in other words, eachof the 52! 
permutations of the deck has to be equally likely. 
Assume that you are given a random number generator which is perfect.
"""

def shuffleV1():
    """
    While this version of shuffle will build a randomized order
    of cards, it is not a true shuffle because it is not moving
    cards around from a predefined order.
    I'm not sure if this is a perfect shuffle; however, if the
    randomizer is perfect, it should also be a perfect shuffle. 
    """
    loc = []            # location list of cards
    card_check = {}     # hash to track if card already used
    count = 0.0         # counter to see percentage spread
    while len(loc) < 52:
        count += 1
        new_card = random.randint(1, 52)
        if new_card not in card_check:
            card_check[new_card] = 1
            loc.append(new_card)
        else:
            card_check[new_card] += 1
    for i in range(1, 53):
        print "card", i,":",(card_check[i] / count) * 100.0,"%"
    print "location:", loc

# shuffleV1()

def shuffleV2(arr):
    """
    following the Fisher-Yates algorithm. unbiased approach to shuffling
    By moving left and selecting random to the left, you lock in the
    right side thereby reducing the number of times a card is selected
    """
    # shuffle cards
    n = len(arr)
    for i in range(n - 1, 0, -1):   # note: length down to 1
        # Note: the naive way to get random k
        # k = random.randint(n). This will be biased
        # instead, do the following:
        k = random.randint(0, i)    # select left including current
        arr[i], arr[k] = arr[k], arr[i]
    return arr

def shuffleV2book(arr):
    """
    Book solution - similar to Fisher-Yates.
    This is more like the "Inside Out" shuffle
    """
    # shuffle cards
    n = len(arr)
    for i in range(n):              # note: length down to 1
        k = random.randint(0, i)    # select left including current
        arr[i], arr[k] = arr[k], arr[i]
    return arr

def shuffleV2test():
    # set up cards
    cards = [1,2,3,4]
    cards_order = {}
    shuffle_this_many = 10000000
    for i in range(shuffle_this_many):
        shuffle = tuple(shuffleV2book(cards))
        if shuffle in cards_order:
            cards_order[shuffle] += 1
        else:
            cards_order[shuffle] = 1
    # list frequency of permutations of cards
    min_frequency = shuffle_this_many
    max_frequency = 0
    for order, frequency in cards_order.items():
        min_frequency = min(min_frequency, frequency)
        max_frequency = max(max_frequency, frequency)
        print order, frequency, ((frequency / (shuffle_this_many * 1.0)) * 100),"%"
    print "frequency min:", min_frequency, "max:", max_frequency, "diff:", max_frequency - min_frequency

shuffleV2test()
