import json
import yaml

# Open and load the YAML file
with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

# Print the Python dictionary
print(ouryaml)

# Print specific values from the dictionary
print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))

# Output the parsed YAML data in pretty JSON format
print("\n\n")
print(json.dumps(ouryaml, indent=4))
# Fill in this file with the code from parsing YAML exercise
