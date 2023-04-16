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

def add_new_country(country, visit_time, cities):

    
    new = {"country": country,"Cities_visited": cities,"total_visit": visit_time}
    Travel_log.append(new)

add_new_country(country="Russia", visit_time = 2, cities=["Moscow","Saint Paris"])
print(Travel_log[2])