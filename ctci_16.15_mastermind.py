"""
Guess the colors of 4 slots filled with RYGB
If color is guessed, but not right slot - "pseudo hit"
if color and slot are guessed - "hit"
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits

Thoughts:
number of variation 4x4x4x4 - easy peasy
Should design method such that it could be connected to a larger class.

Point of this problem is to code carefully, and design as though it were a
part of a larger class

Note: I think the book solution is incorrect - it outputs some strange results.
"""
def checkSolution(guess, solution, message=[]):
    """
    Given a guess and a solution, return hit, pseudo-hit, correct response
    assume solution is correct length / values
    guess may not be correct length / values

    Returns found solution, True or False
    Updates list structure with generated guess verbiage
    """
    result = Result()

    if len(guess) != 4:
        # invalid guess
        result.message = "Invalid guess. Should be four in length"
        return result
    for i in range(4):
        if guess[i].lower() not in "rygb":
            result.message("Invalid guess. Should be combination of letters R, Y, G or B")
            return result

    track = {}

    for i in range(4):
        if guess[i] == solution[i]:
            ## Hit!
            if guess[i] in track:
                # Check if pseudo
                # can only have hit or pseudo
                # hit overrides pseudo
                if track[guess[i]] == "pseudo":
                    # Update pseudo to hit
                    result.pseudohits -= 1
                    result.hits += 1
                    track[guess[i]] = "hit"
            else:
                # Add hit
                track[guess[i]] = "hit"
                result.hits += 1
        else:
            ## Check for pseudo
            if guess[i] in solution:
                ## Pseudo hit!
                if guess[i] not in track:
                    # Add if not already in track
                    track[guess[i]] = "pseudo"
                    result.pseudohits += 1

    return result

class Result:
    hits = 0
    pseudohits = 0
    message = ""

## V2 - from book
# this version doesn't make any sense
def checkSolutionV2(guess, solution):

    frequencies = [0, 0, 0, 0]
    hits = 0
    pseudoHits = 0
    code = {"B":0, "G":1, "R":2, "Y":3}

    # Compute hits and build frequency table
    for i in range(4):
        if guess[i] == solution[i]:
            hits += 1
        else:
            # Only increment the frequency table (which will be used for pseudo-hits)
            # if it's not a hit. If it's a hit, the slot has already been "used." */
            frequencies[code[guess[i]]] += 1

    # Compute pseudo-hits
    for i in range(4):
        if frequencies[code[guess[i]]] > 0 and guess[i] != solution[i]:
            pseudoHits += 1
            frequencies[code[guess[i]]] -= 1

    print hits, pseudoHits, frequencies

solution = "RGBY"
guess = "GGRR"

message = []
correct =  checkSolution(guess, solution, message)
print "correct:", correct.message, correct.hits, correct.pseudohits

# checkSolutionV2(guess, solution)
