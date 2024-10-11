n = int(input())
a = list(map(int, input().split()))
# print(len(set(a)))
a.sort()

count = 0
i = 0
while i < n:
    while (i<n-1) and (a[i] == a[i+1]):
        i+=1
    count+=1
    i+=1
print(count)
