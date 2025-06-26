def match_outcomes(matches):
    outcomes = []
    for result in matches:
        x, y = map(int, result.split(":"))
        if x > y:
            outcomes.append("Win")
        elif x == y:
            outcomes.append("Draw")
        else:
            outcomes.append("Loss")
    return outcomes

print(match_outcomes(["3:1", "1:1", "0:2"]))  # Output: ["Win", "Draw", "Loss"]


#given a list of match scores in the format "x:y" — where:
#x is my team’s score and y is the opponent’s score

#outcomes = []  # This will hold "Win", "Draw", or "Loss" for each match

#for result in matches:
#This starts a loop. It goes through each item (match score) in the matches list.
#Each match result is stored in the variable result during the loop

#x, y = map(int, result.split(":"))
#Each match result looks like a string "x:y", for example "3:1".
#result.split(":") splits that string into a list like ["3", "1"].
#map(int, ...) converts both strings to integers.
#x becomes the score of the first team, y is the score of the second team.

#return outcomes  # Return the list of outcomes
#After the loop is done, return the full list of outcomes.
