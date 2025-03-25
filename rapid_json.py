import rapidjson

data = {
    "name": "Naman Kaushik",
    "age": 25,
    "city": "Delhi",
    "skills": ["Python", "Flask", "API Development"]
}
# Serialize dictionary to JSON
json_data = rapidjson.dumps(data, indent=4)
print("RapidJSON Serialized:", json_data)

# Deserialize JSON string to dictionary
parsed_data = rapidjson.loads(json_data)
print("RapidJSON Parsed:", parsed_data)
