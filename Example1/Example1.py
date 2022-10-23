from re import I


num = int(input("Enter the number: "))
i = 2 
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"The prime factors of number {old} are given in the list: {lst}")