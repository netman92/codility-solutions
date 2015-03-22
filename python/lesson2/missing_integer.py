def solution(A):
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item - 1] = True

    for index in xrange(len(A) + 1):
        if not occurrence[index]:
            return index + 1


def test():
    assert solution([1, 3, 6, 4, 1, 2]) == 5
    #https://codility.com/demo/results/demo42S7QM-4ET/


if __name__ == "__main__":
    test()