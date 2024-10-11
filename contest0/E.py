def countOperations(cells, n):
    count = 0
    i = 0
    while i < n:
        if cells[i] == '#':
            i+=1

        else:
            if i+2 < n:
                if cells[i] == '.' and cells[i+1] == '.' and cells[i+2] == '.':
                    count = 2
                    break
                else:
                    count += 1
                    i+=1
            else:
                count += 1
                i+=1
                
    return count

for _ in range(int(input())):
    n = int(input())
    cells = [i.strip() for i in input()]

    count = countOperations(cells, n)
    print(count)
