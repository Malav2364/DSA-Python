n = int(input("Enter the range for printing ODD numbers : "))
odd_numbers = []
for i in range(0,n):
    if i % 2 == 1:
        odd_numbers.append(i)

print(odd_numbers)