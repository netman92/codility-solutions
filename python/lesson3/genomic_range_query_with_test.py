def solution(S, P, Q):
    impact = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }
    result = list()
    for index in xrange(len(P)):
        minimal = 10
        for nuc in S[P[index]:Q[index] + 1]:
            minimal = min(impact[nuc], minimal)
            if minimal == 1:
                break
        result.append(minimal)

    return result


def test():
    assert solution("CAGCCTA", [2,5,0], [4,5,6]) == [2,4,1]
    # https://codility.com/demo/results/demoNW3MQS-SJG/


if __name__ == "__main__":
    test()