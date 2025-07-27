import math

def movie(card, ticket, perc):
    n = 0
    total_b = card
    current_ticket_price = ticket * perc
    
    while math.ceil(total_b) >= ticket * n:
        n += 1
        total_b += current_ticket_price
        current_ticket_price *= perc  # Each ticket is perc * previous ticket
    
    return n

print(movie(500, 15, 0.9))   # Output: 43
print(movie(100, 10, 0.95))  # Output: 24


# System A is just: n * ticket
# System B is:
# Start with the card price
# First ticket: ticket * perc
# Second ticket: (ticket * perc) * perc, and so on
# keep looping until:
# ceil(system B total) < system A total
