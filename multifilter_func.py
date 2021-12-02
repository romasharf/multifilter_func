#Function that returns list of all elements of the "fil_list" which has at least one pattern from the "patterns" list
def multifilter_func(fil_list = [], patterns = []):
    resulting_list = []
    for pat in patterns:
        for match in fil_list:
            if pat in match:
                resulting_list.append(match)
    return resulting_list
