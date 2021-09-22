print("Welcome to MyDay!")
print("Answer the questions below to control my day.")
print("---------------------------------------------")

day = raw_input("Enter a day of a week: ")
time1 = raw_input("Enter a time in a day: ")
things1 = raw_input("Enter three things I do before breakfast: ")
food1 = raw_input("What do you want me to eat for breakfast? ")
transportation = raw_input("How do you want me to go to school? ")
color1 = raw_input("Enter a color: ")
color2 = raw_input("Enter a color: ")
color3 = raw_input("Enter a color: ")
things2 = raw_input("What do I do at school? ")
time2 = raw_input("Enter a digit: ")
place = raw_input("Enter a place: ")
things3 = raw_input("What or who do I meet on the way? ")
things4 = raw_input("What do we do? ")
words = raw_input("What do she/he/it say to me? ")
foods2 = raw_input("Enter three foods: ")
time3 = raw_input("Enter a time in a day: ")
noun = raw_input("Enter a noun: ")
things5 = raw_input("What do I do before bed? ")
adjective = raw_input("Enter an adjective: ")

story = "Today is " + day + "." + " I wake up at " + time1 + "." + " Then I " + things1 + ". "\
"After that, I have " + food1 + " for breakfast. When I finish breakfast, I get ready to " + transportation + " to school. "\
"I wear a " + color1 + " top, " + color2 + " pants and " + color3 + " shoes today. I " + things2 + " for " + time2 + " hours. "\
"Then I leave the school and get ready to go to the " + place + ". And on the way there, I meet a " + things3 + ". "\
"We " + things4 + " together. She/he/it says: " + words + ". Before going home, I go to the supermarket to buy " + foods2 + " for dinner. "\
"I arrive home at " + time3 + ", eat dinner and watch a video about " + noun + ". After that I lie in bed and " + things5 + " until I fall asleep. "\
"What a " + adjective + " day!"

print(story)