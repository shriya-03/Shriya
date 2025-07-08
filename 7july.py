#repeat nos
def repeat_digits(digits):
    return [[int(d)] * int(d) for d in digits]

print(repeat_digits("1230")) #[[1], [2, 2], [3, 3, 3], []]


#Each digit d is repeated d times in its own sublist

#Now for each character d:
#int(d) converts the character to a number.
#[int(d)] * int(d) creates a list with that number repeated that many times.

#So:
#'1' → int('1') = 1 → [1] * 1 → [1]
#'2' → int('2') = 2 → [2] * 2 → [2, 2]
#'3' → int('3') = 3 → [3] * 3 → [3, 3, 3]
#'0' → int('0') = 0 → [0] * 0 → [] (an empty list)