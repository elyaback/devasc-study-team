import json
import yaml

# Open and load the JSON file
with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

# Print the Python dictionary
print(ourjson)

# Print specific values from the dictionary
print("The access token is {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

# Output the parsed JSON data in YAML format
print("\n\n---")
print(yaml.dump(ourjson))# Fill in this file with the code from parsing JSON exercise
