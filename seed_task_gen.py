import json
import pandas as pd
import codecs

with codecs.open('./new_seeds.csv', 'r', encoding='utf-8', errors='replace') as file:
    df = pd.read_csv(file)

def transform_dataframe(df):
    # Initialize an empty list to store the dictionaries
    json_list = []

    # Loop through each row in the dataframe
    for idx, row in df.iterrows():
        # Create a dictionary for each row
        dict_ = {'id': 'seed_task_' + str(idx),
                 'name': 'explain_behavior',
                 'instruction': row['instruction'],
                 'instances': [{'input': row['input'], 'output': row['output']}],
                 'is_classification': False}

        # Append the dictionary to the list
        json_list.append(dict_)

    # Return the list of dictionaries
    return json_list

# Call the function
json_list = transform_dataframe(df)

# Save the JSON to a file
with open('./new_seeds.json', 'w') as f:
    json.dump(json_list, f)