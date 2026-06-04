import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# exercise 1: return all numbers that are divisible by 3
def return_divisibleby3(limit, divisor):
    """
    round 1: return all numbers that are divisible by 3
    round 2: make it so that the limit and divisor are parameterizable
    """
    retval = []
    for i in range(limit):
        number = i + 1
        if 0 == number % divisor:
            retval.append((number))
    return retval

# exercise 2: merge two dictionaries
def merge_dictionaries(d1, d2) -> dict():
    """
    key question: should we return one of the original dictionaries?
    """

    retval = {}

    max_length = len(d1)
    long_dict = d1
    short_dict = d2
    if len(d2) > max_length:
        long_dict = d2
        short_dict = d1

    for key in long_dict:
        val = long_dict[key]
        if key in short_dict:
            s_val = short_dict[key]
            short_dict[key] = s_val + val
        else:
            val = long_dict[key]
            short_dict[key] = val

    return short_dict

# exercise 3: remove duplicate values from a list
def remove_dup(list_int) -> []:
    history = set()
    retval = []
    for num in list_int:
        if num not in history:
            retval.append(num)
            history.add(num)

    return retval

# exercise 4: remove duplicate values from a list, but the last instance should remain
def remove_dup_2(list_int) -> []:
    history = set()
    retval = []
    for i in range(len(list_int)):
        pos = len(list_int) - i - 1
        num = list_int[pos]
        if num not in history:
            retval.append(num)
            history.add(num)

    return list(reversed(retval))


def main():
    # create a list of numbers 1-20 and then return the ones divisible by 3
    print(return_divisibleby3(20, 3))

    # two dictionaries, merge the values, if the keys match, sum the values
    d1 = {}
    d1[1] = 10
    d1[2] = 20

    d2 = {}
    d2[2] = 30
    d2[3] = 40
    d2[4] = 50

    print(merge_dictionaries(d1, d2))

    # list of integers, remove duplicates, while preserving the order the list

    list_integers = []
    list_integers.append(0)
    list_integers.append(1)
    list_integers.append(2)
    list_integers.append(0)
    list_integers.append(3)
    list_integers.append(0)
    print(remove_dup(list_integers))

    print(remove_dup_2(list_integers))

if __name__ == "__main__":
    main()
