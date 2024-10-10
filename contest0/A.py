n = int(input())
nums = list(map(int, input().split()))

sum_of_n_nums = (n*(n+1))/2

sum_of_givenNums = 0
for i in nums:
    sum_of_givenNums += i

print(int(abs(sum_of_n_nums-sum_of_givenNums)))