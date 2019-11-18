dict01 = {
    'a': 1,
    'b': 2,
}
print(dict01)

dict02 = {value: key for key, value in dict01.items()}

print(dict02)
