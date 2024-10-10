# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)


def trailling_zeros(n):
    if n < 0:
        return None
    
    count = 0
    while n != 0:
        n = n//5
        count += n
    return count

n = int(input())
# print(factorial(n))
num_of_trailing_zeros = trailling_zeros(n)
print(num_of_trailing_zeros)

# print(n%5)
# print(n//5)