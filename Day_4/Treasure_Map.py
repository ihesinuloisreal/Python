row1 = ["M1","M2","M3"]
row2 = ["M2","M3","M4"]
row3 = ["M3","M4","M5"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[horizontal - 1]
selected_row[vertical - 1] = "XX"
print(f"{row1}\n{row2}\n{row3}")
