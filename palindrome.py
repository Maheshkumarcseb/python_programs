from collections import Counter
value=input("enter a value:")
if value == value[::-1]:
    print("palindrome")
else:
    print("not palindrome")
counted_dict=Counter(value)
for key in sorted(counted_dict.keys()):
    print(f'{key} appears {counted_dict[key]} times')
