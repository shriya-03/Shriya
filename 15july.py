def kill_count(counselors, jason_intelligence):
    return [name for name, intel in counselors if intel < jason_intelligence]

counselors = [["Chad", 2], ["Tommy", 9], ["Sarah", 5]]
jason = 7

print(kill_count(counselors, jason))  # Output: ['Chad', 'Sarah']

#counselors: A list of lists. Each inner list contains: A name (str),An intelligence score (int)
#jason_intelligence: An int that represents Jason's intelligence level.

#[name for name, intel in counselors if intel < jason_intelligence]
# This means:
# For each counselor, unpack their [name, intel]
# Check if their intelligence is less than Jason’s
# If yes, include their name in the result list

#Jason’s intelligence: 7

# Chad’s intelligence: 2 →  (Jason is smarter)
# Tommy’s intelligence: 9 →  (Jason is not smarter)
# Sarah’s intelligence: 5 →  (Jason is smarter)
#  So, Jason can outsmart and kill Chad and Sarah.


