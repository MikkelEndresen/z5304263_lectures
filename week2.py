lst_a = ['a']
lst_b = ['b', lst_a]
lst_c = ['b', ['a']]

lst_c[1].append("c")

print(lst_a)
print(lst_b)
print(lst_c)