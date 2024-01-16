my_dict = {"name":"daljeet", "age":25}
print(my_dict["name"])
my_dict["college"] = "GGM"
print(my_dict)
del my_dict["age"]

print(my_dict)

for key , value in my_dict.items():
       print(f"{key}:{value}")
