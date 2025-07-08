def letter_steps(s):
    return [[chr(c) for c in range(ord('A'), ord(ch)+1)] for ch in s]

print(letter_steps("BCDA")) #[['A', 'B'], ['A', 'B', 'C'], ['A', 'B', 'C', 'D'], ['A']]


#ord(ch): Converts a character ch into its Unicode (ASCII) integer code.
#Example: ord('A') is 65, ord('C') is 67.
#chr(code): Converts an integer code back into a character.
#Example: chr(65) is 'A', chr(67) is 'C'.
#range(start, end+1): Produces numbers from start up to end (inclusive, because of +1).

#'B'
#ord('B') = 66
#range(ord('A'), ord('B') + 1) → range(65, 67) → [65, 66]
#Convert each to characters: chr(65) = 'A', chr(66) = 'B'
#Result: ['A', 'B']