lst = list(map(int, input("Enter numbers separated by spaces:\n").split()))
print(f"Source list: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"List of non-repeating elements: {new_lst}")