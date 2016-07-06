import requests, json

class Muscle:

    def __init__(self, id, is_front, name):
        self.id = id
        self.is_front = is_front
        self.name = name


r = requests.get("https://wger.de/api/v2/muscle.json")
data = json.loads(r.text)
print "Qty of muscles: ", data['count']
muscles = []
for muscle in data["results"]:
    muscles.append(Muscle(muscle["id"], muscle["is_front"], muscle["name"]))
