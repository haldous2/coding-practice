"""
Implement an algorithm to return a list of matching words, 
  given a sequence of digits. 
You are provided a list of valid words
(provided in whatever data structure you'd like). 

With pre-defined words, test numeric input and return matching words

Note: I started with the most optimal method - the book method mentions
      building string prefixes and matching them, and even using a trie
      to speed things up. Thinking about a trie, that seems like it would
      be best for situations where users were entering letters to retrieve
      text.
      Also note that the book says lookups are O(n), where n is the length 
      of the number - my thinking on this is that, as the user enters in the
      number, results are displayes .. e.g., enters 8, then 83, then 832 etc.
      Thus O(n), one lookup for each digit.

Brute force: Generate all permutations for all letters in number - this 
             will generate up to 16! permutations - too many!
Optimized:   Convert all strings to number, then return list with 
             matching number
Better:      Only convert strings to number where the first letter
             of the string matches the first mapped digit of the number
             e.g. 3=a,b,c etc.
             Of course, the list of words could also be preprocessed 
             ahead of time, and the Optimized version would be faster.

Map:
1 - 
2 - abc
3 - def
4 - ghi
5 - jkl
6 - mno
7 - pqrs
8 - tuv
9 - wxyz
0 -
"""
strings = []               # given
map_nbr_str = {}           # the end goal
map_nbr_ltr = {}           # reverse lookup (not used for optimal)
map_ltr_nbr = {}           # reverse lookup

map_nbr_ltr[2] = ["a","b","c"]
map_nbr_ltr[3] = ["d","e","f"]
map_nbr_ltr[4] = ["g","h","i"]
map_nbr_ltr[5] = ["j","k","l"]
map_nbr_ltr[6] = ["m","n","o"]
map_nbr_ltr[7] = ["p","q","r","s"]
map_nbr_ltr[8] = ["t","u","v"]
map_nbr_ltr[9] = ["w","x","y","z"]

map_ltr_nbr["a"] = 2
map_ltr_nbr["b"] = 2
map_ltr_nbr["c"] = 2
map_ltr_nbr["d"] = 3
map_ltr_nbr["e"] = 3
map_ltr_nbr["f"] = 3
map_ltr_nbr["g"] = 4
map_ltr_nbr["h"] = 4
map_ltr_nbr["i"] = 4
map_ltr_nbr["j"] = 5
map_ltr_nbr["k"] = 5
map_ltr_nbr["l"] = 5
map_ltr_nbr["m"] = 6
map_ltr_nbr["n"] = 6
map_ltr_nbr["o"] = 6
map_ltr_nbr["p"] = 7
map_ltr_nbr["q"] = 7
map_ltr_nbr["r"] = 7
map_ltr_nbr["s"] = 7
map_ltr_nbr["t"] = 8
map_ltr_nbr["u"] = 8
map_ltr_nbr["v"] = 8
map_ltr_nbr["w"] = 9
map_ltr_nbr["x"] = 9
map_ltr_nbr["y"] = 9
map_ltr_nbr["z"] = 9

# 2255  abc abc jkl jkl
strings.append("ball")
strings.append("call")
strings.append("balk")

# 8733  tuv pqrs def def
strings.append("tree")
strings.append("used")

def match_t9_to_string(strings, number):
    """
    Return strings that match number
    """
    if number in map_nbr_str:
        return map_nbr_str[number]
    return []

def map_strings_to_numbers(strings):
    """
    Convert strings to number and store in dictionary
    """
    for string in strings:
        new_number = ""
        for letter in string:
            new_number += str(map_ltr_nbr[letter])
        if int(new_number) in map_nbr_str:
            map_nbr_str[int(new_number)].append(string)
        else:
            map_nbr_str[int(new_number)] = [string]

# Preprocessor - builds number to string hash table
map_strings_to_numbers(strings)

# Testing
number = 8733
# number = 2255
print match_t9_to_string(strings, number)
