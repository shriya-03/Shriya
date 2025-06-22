def season_of(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in[9,10,11]:
        return "Autumn"
    else:
        return "Please enter a number within the range of 1 to 12"

print(season_of(3))   # Output: Spring
print(season_of(8))   # Output: Summer
print(season_of(100))  # Output: Please enter a number within the range of 1 to 12

