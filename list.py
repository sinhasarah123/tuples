
n = int(input("Enter a number: "))


odd_numbers = [i for i in range(1, n) if i % 2 != 0]
even_numbers = [i for i in range(1, n) if i % 2 == 0]


print("Odd numbers under", n, ":", odd_numbers)
print("Even numbers under", n, ":", even_numbers)