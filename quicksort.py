def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst.pop()
    lhs = [e for e in lst if e <= pivot]
    rhs = [e for e in lst if e > pivot]
    return quicksort(lhs) + [pivot] + quicksort(rhs)

print(quicksort([
    int(n) for n in input(
        'input space seperated numbers: '
    ).split()
]))
