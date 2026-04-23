def solution(arr, queries):
    for querey in queries:
        i, j = querey
        arr[i], arr[j] = arr[j], arr[i]
    return arr