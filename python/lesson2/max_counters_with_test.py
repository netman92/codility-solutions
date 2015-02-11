#https://codility.com/demo/results/demoE4YC2V-CQ7/

def solution(N, A):
    to_return = [0]*N
    max_counter = 0
    current_max_counter = 0

    for index in A:
        if 1 <= index <= N:
            if max_counter > to_return[index-1]:
                to_return[index-1] = max_counter
            to_return[index-1] += 1

            #max
            if current_max_counter < to_return[index-1]:
                current_max_counter = to_return[index-1]
        else:
            max_counter = current_max_counter

    for index in range(0, N):
        if to_return[index] < max_counter:
            to_return[index] = max_counter

    return to_return


def test():
    assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]

if __name__ == "__main__":
    test()