"""
Living People
Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. 
You may assume that all people were born between 1900 and 2000 (inclusive). 
If a person was alive during any portion of that year, they should
be included in that year's count. 
For example, Person (birth= 1908, death= 1909) is included 1908 and 1909

Assumptions
1. All people born between 1900 and 2000
2. data is current, and we are not looking into the future
3. data is correct, date of birth and other dates are in the correct order

Notes about Cracking the coding interview solution
   I find the solution to be lacking in the book. This solution loosely resembles
   the final 'more optimized' version, though it returns all dates that have max
   people alive, and not just a single date. 
   The time for this solution is O(P) + O(Y). It seems that O(Y) might be a 
   constant, and therefor the time might just be O(P)
"""
range_year_start = 1900
range_year_end = 2000

class Person:
    def __init__(self, name, dob):
        """
        For brevity - assume dod, dob are stored as year only
        will mess with actual dates on next increment
        """
        self.name = name
        self.dob = dob
        self.dod = None

    def setDOD(self, dod):
        self.dod = dod

    def getDOB(self):
        return self.dob

    def getDOD(self):
        return self.dod

    # comparator
    def isalive(self, year):
        """
        Is alive if date of birth and date of death are between date given
        if date of death not set, assume person still alive
        """
        if self.dod:
            if self.dob <= year and self.dod >= year:
                return True
        else:
            if self.dob <= date:
                return True
        return False

def find_year_most_alive():
    """
    """
    people = []

    ## Test 1 - many people even spaced
    year_start = 1900 ## test data
    years_lived = 50  ## test data
    for i in range(25):
        person = Person(i, year_start)
        person.setDOD(year_start + years_lived)
        people.append(person)
        year_start += 1

    ## Test 2 - same dates
    # person = Person(1, 1950)
    # person.setDOD(1950)
    # people.append(person)
    # person = Person(1, 1951)
    # person.setDOD(1951)
    # people.append(person)
    # person = Person(1, 1951)
    # person.setDOD(1951)
    # people.append(person)

    date_hash = {}
    count_people_by_date(people, date_hash)
    count_hash = {}
    maxcount = organize_dates_by_count(date_hash, count_hash)

    # print_people(people)
    # print "dates:", date_hash
    # print "count:", count_hash
    # print "maxcount:", maxcount
    if count_hash:
        print "dates for maxcount:", count_hash[maxcount]
    else:
        print "no dates found"

def print_people(people):
    for person in people:
        print person.name, person.dob, person.dod

def count_people_by_date(people, date_hash):
    """
    Count people by date time: O(n) number of people
    Create date_hash[year] = number of people
    """
    for person in people:
        year_start = max(person.getDOB(), range_year_start)
        year_end = person.getDOD()
        if year_end is not None:
            year_end = min(year_end, range_year_end)
        else:
            year_end = range_year_end
        for i in range(year_start, year_end + 1):
            if i in date_hash:
                date_hash[i] += 1
            else:
                date_hash[i] = 1   

def organize_dates_by_count(date_hash, count_hash):
    """
    Organize dates by count time: O(1000) date range
    Create count_hash[number of people] = [dates] from date_hash
    Also need to track max
    """
    maxcount = 0
    if date_hash:
        for key, val in date_hash.items():
            maxcount = max(maxcount, val)
            if val in count_hash:
                count_hash[val].append(key)
            else:
                count_hash[val] = [key]
        return maxcount

find_year_most_alive()
