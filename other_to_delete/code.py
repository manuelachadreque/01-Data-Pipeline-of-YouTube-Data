import pandas as pd
import numpy as np

print("hello")

import json

# Path to your JSON file
file_path = 'Data/CA_category_id.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the data to verify
kind=data['kind']
etag=data['etag']
items=data['items']



items1 = pd.json_normalize(items)
print(items)