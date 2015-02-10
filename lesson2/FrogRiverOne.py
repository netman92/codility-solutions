def solution(X, A):
    items = set()
    index = 0
    for i in A:
        items.add(i)
        if X == len(items):
            return index
        index += 1
    return -1


def test():
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
    assert solution(7, [1, 3, 1, 4, 2, 3, 5, 4]) == -1
    assert solution(2, [2, 1]) == 1

if __name__ == "__main__":
    test()