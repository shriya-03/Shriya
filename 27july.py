# System A: Each game costs $60.
# System B: Subscription = $300 + first game = $45, then each next game costs 95% of the previous game’s price.
# We want to find the minimum number of games after which System B becomes cheaper than System A.

import math

def gaming_subscription(subscription, game_price, first_discount, perc):
    n = 0
    costA = 0
    costB = subscription
    current_game = game_price * first_discount
    
    while True:
        n += 1
        costA += game_price
        costB += current_game
        current_game *= perc   # price reduces for next game
        
        if math.ceil(costB) < costA:
            return n

print(gaming_subscription(300, 60, 0.75, 0.95))


# The function gaming_subscription() compares two different ways of buying games to determine after how many games the subscription becomes cheaper than buying games individually.
# Inputs:
# subscription: the initial cost of the subscription.
# game_price: the price of a single game if bought individually.
# first_discount: the discount factor for the first game with the subscription (e.g., 0.75 means 25% off).
# perc: the percentage (factor) by which each subsequent game gets cheaper under the subscription.


# n = 0                  number of games purchased
# costA = 0              total cost of buying without subscription
# costB = subscription  total cost of subscription (starts with just the sub cost)
# current_game = game_price * first_discount   first discounted game price

# while True:
#     n += 1
#     costA += game_price                 add full price to Plan A
#     costB += current_game             add discounted price to Plan B
#     current_game *= perc               reduce price for next game
    
#     if math.ceil(costB) < costA:       when Plan B becomes cheaper
#         return n
