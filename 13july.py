def add_greetings(developers):
    for dev in developers:
        dev['greeting'] = f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"
    return developers
list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
]

updated_list = add_greetings(list1)
for dev in updated_list:
    print(dev['greeting'])
