
def first_two(str):
    if len(str) <= 2:
        return str
    else:
        sub_string = str[0:2]
        return sub_string

print(first_two("hello"))
print(first_two("ab"))