# a1 b1 c1
# a2 b2 c2
# a3 b2 c3
line1 = ["⬜️","️⬜️","️⬜️",]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter your area in row and coloum in this in put: ") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
import random
split= position[0].lower()
abc=["a","b","c"]
letter_index= abc.index(split)
num_index= int(position[1])-1
map[num_index] [letter_index]  ="X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print('   a','    b','    c')
print(f"{line1}\n{line2}\n{line3}")