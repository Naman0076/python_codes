import json

data = {
    "name": "Naman",
    "age": 21,
    "city": "Delhi",
    "skills": ["Python", "Flask", "API Development"]
}
# Convert Python dictionary to JSON string
json_data = json.dumps(data, indent=4)
print("Serialized JSON:", json_data)

# Convert JSON string back to Python dictionary
parsed_data = json.loads(json_data)
print("Parsed Python Object:", parsed_data)

# Writing JSON to a file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading JSON from a file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print("Loaded JSON from file:", loaded_data)
