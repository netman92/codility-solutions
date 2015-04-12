from bisect import bisect_right


def solution(A):
    pairs = 0
    intervals = sorted([(i - A[i], i + A[i]) for i in range(len(A))])
    starts = [i[0] for i in intervals]
    for i in range(len(starts)):
        disk_end = intervals[i][1]
        count = bisect_right(starts, disk_end) # binary search get count of elements <= disks_end
        count -= (i + 1)  # minus allready founded
        pairs += count
        if pairs > 10000000:
            return -1
    return pairs


def test():
    assert solution([1, 5, 2, 1, 4, 0]) == 11
    # https://codility.com/demo/results/demoKP2N5N-EY2/


if __name__ == "__main__":
    test()