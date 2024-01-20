print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

count1 = 0
count2 = 0

count1 += lower_name1.count("t")
count1 += lower_name2.count("t")
count1 += lower_name1.count("r")
count1 += lower_name2.count("r")
count1 += lower_name1.count("u")
count1 += lower_name2.count("u")
count1 += lower_name1.count("e")
count1 += lower_name2.count("e")
count2 += lower_name1.count("l")
count2 += lower_name2.count("l")
count2 += lower_name1.count("o")
count2 += lower_name2.count("o")
count2 += lower_name1.count("v")
count2 += lower_name2.count("v")
count2 += lower_name1.count("e")
count2 += lower_name2.count("e")

count = str(count1) + str(count2)

if int(count) < 10 or int(count) > 90:
  print(f"Your score is {count}, you go together like coke and mentos.")
elif int(count) >= 40 and int(count) <= 50:
  print(f"Your score is {count}, you are alright together.")
else:
  print(f"Your score is {count}.")
