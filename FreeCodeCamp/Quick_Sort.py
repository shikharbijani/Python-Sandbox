def quick_sort(values):
    if len(values) <= 1:
        return values[:]

    pivot = values[0]

    less = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    greater = [x for x in values if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)
