def solution(A):
    length = len(A)
    arr_sum = sum(range(0, length+2))

    for elem in A:
        arr_sum = arr_sum - elem

    return arr_sum


def test():
    assert solution([2, 3, 1, 5]) == 4
    assert solution([2, 3, 1, 5, 4]) == 6
    assert solution([]) == 1

if __name__ == "__main__":
    test()