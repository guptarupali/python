my_string = "this is a sample string"
my_string_spilt = my_string.split(sep=" ", maxsplit=1)
print(my_string_spilt)

my_string_spilt2 = my_string.rsplit(sep= " ", maxsplit= 2)
print(my_string_spilt2)

my_string_spilt3= my_string.split(sep=" ")
print(my_string_spilt3)

my_string2 = "this is sample \n string"
print(my_string2)
my_string2.splitlines()
print((my_string2))

my_list = ["this", "is", "a", "string"]
print(" ".join(my_list))

my_string3 = " this is sample string \n"
print(my_string3.strip())

print(my_string3.rstrip())
print(my_string3.lstrip())