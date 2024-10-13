def play(n):
    if (n%3 == 0) and n<3:
        return "First"
    
    if n%3 == 0:
        return "Second"

    if (n+1)%3 == 0 or (n-1)%3 == 0:
        return "First"
    else:
        return "Second"


for _ in range(int(input())):
    n = int(input())
    print(play(n))