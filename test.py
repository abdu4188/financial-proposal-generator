selectedNotes = [0,2,3]
# print(selectedNotes)
temp = [0,1,2,3,4,5,6]
for selected in selectedNotes:
    print("selected"+str(selected))
    temp[selected]= None

print(temp)