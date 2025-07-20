def monkeys():
 for i in range(5,0,-1):
   print(f"{i} little monkey{'s'*(i!=1)} jumping on the bed,\nOne fell off and bumped his head,\nMama called the doctor and the doctor said,\n'No more monkeys jumping on the bed!'\n")

mon=monkeys()

# loop that starts with i = 5 and counts downward to 1 (not including 0), decreasing by 1 each time.
# So it will run with:
# i = 5
# i = 4
# i = 3
# i = 2
# i = 1

#then prints a nursery rhyme-style verse for each number of monkeys.
# Let’s break it down:
# f"{i} little monkey{'s'*(i!=1)} jumping on the bed,
# This uses an f-string to insert the value of i.
# If i != 1, it adds an "s" after "monkey" (so we get "monkeys").
# If i == 1, it adds nothing (so it stays "monkey").
# Then the rest of the lines are printed as part of the verse, with \n meaning a new line.