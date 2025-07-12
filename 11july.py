def get_python(devs):
    for dev in devs:
        if dev['language'] == 'Python':
            return dev['first_name'] + ", " + dev['country']
    return "There will be no Python developers"


list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]

print(get_python(list1))  # Output: Victoria, Puerto Rico
