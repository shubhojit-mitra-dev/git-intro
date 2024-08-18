import json

class Data:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def to_json(self):
        return json.dumps(self.__dict__)

# Create an instance of the Data class
data = Data("John Doe", 25, "New York")

# Convert the data object to a JSON string
json_data = data.to_json()

# Print the JSON string
print(json_data)