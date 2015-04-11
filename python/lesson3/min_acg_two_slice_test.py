def solution(A):
    minimal_index = None
    minimal = 10**5
    for index, number in enumerate(A):
        if index > len(A)-2:
            break
        current_avg = sum(A[index:index+2])/2.0
        if current_avg < minimal:
            minimal_index = index
            minimal = current_avg

        if index > len(A)-3:
            continue
        current_avg = sum(A[index:index+3])/3.0
        if current_avg < minimal:
            minimal_index = index
            minimal = current_avg
    return minimal_index


def test():
    assert solution([4,2,2,5,1,5,8]) ==1
    #https://codility.com/demo/results/demoYG5UAN-QJ8/

if __name__ == "__main__":
    test()