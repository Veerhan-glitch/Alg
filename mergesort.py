# A function sorting a given list using the MergeSort algorithm,
# returning a sorted copy of the list.
def mergesort(lst):
    # Return single-element lists
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = mergesort(left)
    right = mergesort(right)

    res = []

    # Repeat as long as both lists have items
    while min(len(left), len(right)) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    # Append leftover items
    for item in left:
        res.append(item)
    for item in right:
        res.append(item)

    return res
