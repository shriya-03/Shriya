def missing_word(nums, comment):
    cleaned = comment.replace(" ", "")
    try:
        return ''.join([cleaned[i] for i in nums]).lower()
    except IndexError:
        return "No mission today"
print(missing_word([5, 0, 3], "I Love You"))  
# Cleaned comment: "ILoveYou"
# Indexes: 5 → 'Y', 0 → 'I', 3 → 'v' → Result: 'ivy'
