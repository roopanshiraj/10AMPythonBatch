dict1 = {"jack": 4098, "sape": 4139}
dict1["guido"] = 4127
print(dict1)
print(dict1["jack"])
del dict1["sape"]
print(dict1)
dict1["irv"] = 4127
print(dict1)
a=(list(dict1))
print(a)
print(sorted(dict1))
print('guido' in dict1)
print('jack' not in dict1)

