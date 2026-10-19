#list
#print list
#access specifit element of list
#print list with comment
#modify list
#add element to end of the list(append)
#insert element to list
#remove element from a list(del) or (pop()) or by value



    # use variables then equals sign(=) then [] and inside square brackets use the item in quatation.
    ## variable = ["item1", "item2", "item3"]
name = ["Goku", "Rimuru", "Diablo", "Vegeta", "Veldora", "Itachi", "Obito", "Gabimaru", "Gojo", "Toji"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(name)
print(numbers)
#To access a particular item from a list use the index inside [] after the variable name
print(name[2].upper())
print(numbers[3]) # Index position starts at 0, not at 1
#To use individual values from list in a comment use the f-strings with the list index.
print(f"{name[0].upper()} is the no {numbers[0]} fighter")
    #To modify a element in a list use the variable name then the square brackets and inside it
    ##use the index of the element you want to modify then equalto "=" then inside quotes type 
    ###the modified element
    ####To modify perticular element, use list_name[index_number] = "modified_element"
name[4] = "Goten"
numbers[9] = 20
print(name)
print(numbers)
#To add element at the end, use list_name.append("new_element")
name.append("Gohan")
print(name)
#To insert a element at any place of the list, use list_name.insert(index_number, "new_element")
name.insert(1, "Zeno")
print(name)
#To remove element from a list, use del list_name[index_number]
del name[8]
print(name)
#To remove element from a list and store it in a variable use list_name.pop(index_number)
deleted = name.pop(-3), name.pop(-2)
print(name)
print(deleted)
#To remove item by value, use list_name.remove("element_name")
name.remove("Goten")
print(name)
#To remove by variable, use list_name.remove(variable_name)
rem = "Gohan"
if rem in name:
    name.remove(rem)
print(name)
print(f"we removed {rem} from the list")

