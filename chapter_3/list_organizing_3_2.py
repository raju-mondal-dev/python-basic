#sort permanently
#sort temporarily
#reverse
#finding length of a list



cars = ["bmw", "supra", "audi", "rolls-royce", "ferrari", "porsche"]
print(cars)
#To sort an list permanently, use list_name.sort()
cars.sort()
print(cars)
#To sort a list by reverse order permanently, use list_name.sort(reverse=True) [reverse=True is argument}
cars.sort(reverse = True)
#To sort a list temporarily, use sorted(list_name)
print(cars)
d = sorted(cars)
print(d)
print(sorted(cars))
print(cars)
    #If list originally stored in chronological order, use reverse() method to sort them reverse
    ##use list_name.reverse()
cars.reverse()
print(cars)
#To find the length of a list, use len(list_name)
length = len(cars)
print(length)