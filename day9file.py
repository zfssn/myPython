def is_palindrome(n):
    n1=str(n)
    n2=n1[::-1]
    if n1==n2:
       return n

output = filter(is_palindrome, range(1, 1000))
print(list(output))
# is_palindrome(101)