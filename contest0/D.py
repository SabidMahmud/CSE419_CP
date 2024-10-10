for _ in range(int(input())):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))
    dist = [stations[0]]

    for i in range(0, n-1):
        dist.append(abs(stations[i] - stations[i+1]))
    
    dist.append(abs(x - stations[-1])*2)
    print(max(dist))
        