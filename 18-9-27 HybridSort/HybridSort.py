def merge_sort(unsorted, threshold, reverse):
    """
     Use merge sort (Recursively!) to sort and return the list unsorted.
    :param unsorted:
    :param threshold:
    :param reverse:
    :return:
    """
    if not threshold:
        threshold = 1
    if len(unsorted) <= threshold:
        return insertion_sort(unsorted, reverse)
    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    left = merge_sort(left, threshold, reverse)
    right = merge_sort(right, threshold, reverse)
    return merge(left, right, reverse)


def merge(first, second, reverse):
    """
    Given two lists, first and second, merge them into a single, sorted list and return it.
    :param first:
    :param second:
    :param reverse:
    :return:
    """
    result = []
    if not reverse:
        while len(first) > 0 and len(second) > 0:
            if first[0] <= second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        if first:
            result += first
        if second:
            result += second
    else:
        while first and second:
            if first[0] >= second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        if first:
            result += first
        if second:
            result += second
    return result


def insertion_sort(unsorted, reverse):
    """
    Use Insertion Sort to sort and return the list unsorted
    :param unsorted:
    :param reverse:
    :return:
    """
    if not reverse:
        n = len(unsorted)
        if n == 1:
            return unsorted
        for i in range(1, n):
            for j in range(i, 0, -1):
                if unsorted[j] <= unsorted[j - 1]:
                    unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                else:
                    break
    else:
        n = len(unsorted)
        if n == 1:
            return unsorted
        for i in range(1, n):
            for j in range(i, 0, -1):
                if unsorted[j] >= unsorted[j - 1]:
                    unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                else:
                    break
    return unsorted
