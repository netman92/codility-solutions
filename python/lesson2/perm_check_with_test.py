def solution(A):
    length = len(A)
    is_permutation = 1
    A.sort()

    for i in range(1, length+1):
        if i != A[i-1]:
            is_permutation = 0
            break

    return is_permutation


def test():
    assert solution([4, 1, 3, 2]) == 1
    assert solution([4, 1, 3]) == 0
    assert solution([4, 1, 3, 2, 5, 5, 2]) == 0

if __name__ == "__main__":
    test()