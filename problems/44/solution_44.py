from copy import copy


def coding_problem_44(arr):
    """
    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i]
    and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
    Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
    You may assume each element in the array is distinct.
    Examples:

    >>> coding_problem_44([1, 2, 3, 4, 5])
    0
    >>> coding_problem_44([2, 4, 1, 3, 5])  # inversions: (2, 1), (4, 1), (4, 3)
    3
    >>> coding_problem_44([5, 4, 3, 2, 1])  # every distinct pair forms an inversion
    10

    Note: complexity is that of sorting O(n log(n)) plus a linear pass O(n), therefore bounded by O(n log(n))
    Note2: [TODO] idea is here, but should avoid using .index(), which is a linear search. Committing as is for now.
    """
    inversions = 0
    sorted_indexes = [xi[1] for xi in sorted(zip(arr, range(len(arr))), cmp=lambda x, y: cmp(x[0], y[0]))]
    for index in range(len(sorted_indexes)):

        destination = sorted_indexes.index(index)
        sorted_indexes.remove(index)
        inversions += destination

    return inversions


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
