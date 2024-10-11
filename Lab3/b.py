n, m, k = map(int, input().split())
desired_size = list(map(int, input().split()))
apartment_size = list(map(int, input().split()))
desired_size.sort()
apartment_size.sort()

res = 0
i = 0
j = 0
while i < n and j < m:
    if abs(desired_size[i] - apartment_size[j]) <= k:
        res += 1
        i += 1
        j += 1
    elif desired_size[i] > apartment_size[j]:
        j += 1
    else:
        i += 1


print(res)