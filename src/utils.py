import random

def roll_dice(sides):
    return random.randint(1, sides)

def split_string(str, max_length=1500):
    '''Takes a string and splits it into a list where each item in the list is no more than 2000 characters and ends on a sentence boundary'''

    if len(str) > max_length:
        substrings = []
        while len(str) > max_length:
            last_boundary_index = str[:max_length].rfind(".")
            if last_boundary_index == -1:
                last_boundary_index = str[:max_length].rfind("?")
                if last_boundary_index == -1:
                    last_boundary_index = str[:max_length].rfind("!")
                    if last_boundary_index == -1:
                        last_boundary_index = max_length
                    else:
                        last_boundary_index += 1
                else:
                    last_boundary_index += 1
            else:
                last_boundary_index += 1
            substrings.append(str[:last_boundary_index])
            str = str[last_boundary_index:]
        substrings.append(str)
        return substrings
    else:
        return [str]