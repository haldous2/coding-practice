"""
Given string, match to pattern of a's and b's
e.g. given "aab" -> match to a string like "catcatgo" etc.

This problem was especially difficult for me. At first I thought
I could solve this using hash tables, hashing values from the
value string, then doing some magic in eliminating the smallest
value from all other strings and doing that until only two strings
were left. I then realized that matching the pattern could be 
achieved in numerous ways - and analyzing the pattern first was
the way to go.

The solution is similar to the book, however, with this solutuion,
I find all possible lengths of a & b that could be viable, and then
test if they match the value
"""
# pattern = "ab"                    # True - although cannot tell where of ab are
# value = "catgo"

pattern = "aabab"                 # True
value = "catchcatchgocatchgo"
# pattern = "aabab"                 # False
# value = "catchcatchgocatchg"

# pattern = "bbaba"
# value = "catchcatchgocatchgo"

# pattern = "abb"
# value = "xxxxxxxxxxyyyyy"

# pattern = "abaabb"
# value = "catchgocatchcatchgogo"

# pattern = "abab"
# value = "catgocatgo"

## Version 1: The great guesser - O(nlogn)?
#  ----------------------------------------------------------------------
def guess_patterns(pattern, value):
    """
    Guess at sizes (educated guesses)
    Use those guesses to match patterns to value
    """

    def verify_pattern_match(pattern, value):
        """
        Main calling function to pattern matcher

        Big-O: O(?)
        """
        if len(pattern) <= 2:
            # cannot evaluate solution with only two letters
            # any combination of a's, b's could make solution
            return True
        sizes = guess_sizes(pattern, value)
        return possiblematches(pattern, value, sizes)

    def guess_sizes(pattern, value):
        """
        Take a guess at the sizes of a, b using pattern and string
        Returns possible sizes for a & b

        Big-O: O(p) where p is length of pattern
        """
        possible = []
        # count a's, b's
        number_of_a = 0
        number_of_b = 0
        for letter in pattern:
            if letter == "a": 
                number_of_a += 1
            else:
                number_of_b += 1
        # cannot make a guess if not enough a's or b's
        if number_of_a == 0 or number_of_b == 0:
            return []
        # start guessing
        counter = 0
        for proposed_length_a in range(1, (len(value) / number_of_a)):

            # need to find a b that evenly divides the rest
            # of the length of value
            value_length = len(value) - (number_of_a * proposed_length_a)
            # b needs to evenly divide into leftover length of value
            if value_length % number_of_b == 0:
                counter += 1
                proposed_length_b = value_length / number_of_b
                length_a = number_of_a * proposed_length_a
                length_b = number_of_b * proposed_length_b
                length_a_b = length_a + length_b
                if (length_a_b == len(value)):
                    possible.append((proposed_length_a, proposed_length_b))

        # print "possible:", possible, "counter:", counter
        return possible

    def possiblematches(pattern, value, possible):
        """
        With possible sizes, look for matches based on pattern
        e.g., with known length of a & b
            read length of a or b based on pattern to verify value
        Returns T or F if match found

        Big-O: O(p*v) where p is length of pattern, v length of value
                      Although, this will be considerably smaller
        """
        if possible:
            for possibility in possible:

                pattern_a = ""
                pattern_b = ""
                # Establish first pattern
                if pattern[0] == "a":
                    pattern_a = value[0:possibility[0]]
                if pattern[0] == "b":
                    pattern_b = value[0:possibility[1]]
                if not pattern_a:
                    # Find wheere pattern 'a' starts
                    pattern_start = 0
                    for letter in pattern:
                        if letter == "a":
                            break
                        else:
                            # increment pattern start by 'b' length
                            pattern_start += possibility[1]
                    # Discover pattern value
                    pattern_a = value[pattern_start:pattern_start + possibility[0]]
                if not pattern_b:
                    # Find wheere pattern 'b' starts
                    pattern_start = 0
                    for letter in pattern:
                        if letter == "b":
                            break
                        else:
                            # increment pattern start by 'a' length
                            pattern_start += possibility[0]
                    # Discover pattern value
                    pattern_b = value[pattern_start:pattern_start + possibility[1]]

                # print "pattern_a", pattern_a, "pattern_b:", pattern_b

                # Build string for comparison
                test_value = ""
                for letter in pattern:
                    if letter == "a":
                        test_value += pattern_a
                    else:
                        test_value += pattern_b
                # print "test_value:", test_value
                if test_value == value:
                    return True

        # Pattern does not match
        return False

    return verify_pattern_match(pattern, value)

print guess_patterns(pattern, value)
