from constants import UNDER_20, TENS, ABOVE_100


def num_to_word(num: int)-> str:
    """
    Convert a number to its word representation.        
    Notes: This function handles numbers from 0 to 999,999,999,999. 

    :param num: The number to convert   
    :return: The word representation of the number
    >>> num_to_word(127643)
    'One hundred twenty Seven thousand Six hundred forty Three'
    >>> num_to_word(0)
    'Zero'
    >>> num_to_word(9)
    'Nine'
    """

    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        reminder = num % 10
        if reminder == 0:
            return TENS[num // 10]
        return TENS[num // 10] + " " + num_to_word(reminder)

    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]

    if num % pivot == 0:
        return f"{p1} {p2}"
    return f"{p1} {p2} {num_to_word(num % pivot)}"
 
if __name__ == '__main__':
    assert num_to_word(0) == "Zero"
    assert num_to_word(9) == "Nine"
    assert num_to_word(10) == "Ten"
    assert num_to_word(15) == "Fifteen"
    assert num_to_word(20) == "twenty"
    assert num_to_word(21) == "twenty One"
    assert num_to_word(127643) =="One hundred twenty Seven thousand Six hundred forty Three"

    print("All tests passed.")