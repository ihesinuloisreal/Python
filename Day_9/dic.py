Capital = {
    "France" : "Paris",
    "Garmany" : "Berlin",
}

# Nesting List in a dictionary
Travel_log = {
    "France": {"Cities_visited" : ["Paris", "Lille", "Dijon"], "total_visit": 12},
    "Garmany": {"Cities_visited" : ["Berlin", "Humburg", "Stuttgart"], "total_visit": 5},
}

# Nesting dictionaryin a dictionary

Cities_visited = {
    "France": {
        "Paris" : "",
        "Lille" : "",
        "Dijon" : "",
    },
    "Germany": {
        "Berlin": "",
        "Humburg": "",
        "Stuttgart": "",
    },
}

# Nesting a dictionaryin a list
Travel_log = [
    {
        "Country":"France", 
        "Cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visit": 12
    },
    {
        "Country":"Garmany", 
        "Cities_visited" : ["Berlin", "Humburg", "Stuttgart"], 
        "total_visit": 5
    },
]