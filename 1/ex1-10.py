days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
    print(x)
    
for x in [1, 2, 3, 4, 5]:
    print(x)


for day in days:
    if day is "Wed":
        break
    else:
        print(day)