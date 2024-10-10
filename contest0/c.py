def check_non_descending(arr, n, k):
    if k == 1:
        return all(arr[i] <= arr[i + 1] for i in range(n - 1))
    
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
        return True

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if (i + 1 - i) > k:
                return False
    
    return True

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print("YES" if check_non_descending(arr, n, k) else "NO")