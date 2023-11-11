import json
from rouge import Rouge  

def calculate_similarity(instruction1, instruction2):
    rouge = Rouge()
    scores = rouge.get_scores(instruction1, instruction2)
    return scores[0]['rouge-1']['f']

with open('new_tasks/regen3.json', 'r') as file:
    data = json.load(file)

updated_data = data.copy()

indices_to_remove = []

for i, item1 in enumerate(data):
    similar_instructions = []
    for j in range(i + 1, len(data)):  # Only compare with instructions after the current instruction
        similarity = calculate_similarity(item1['instruction'], data[j]['instruction'])
        if similarity > 0.9:
            similar_instructions.append((j, data[j]['instruction'], similarity))
    flag = False
    if similar_instructions:
        print(f"Instruction {i + 1}: {item1['instruction']}")
        print("Similar Instructions:")
        for index, instruction, similar in similar_instructions:
            print(f"{index + 1}: {instruction} Similarity: {similar}")
        
            if similar > 0.99:
                indices_to_remove.append(i)
                print(f"Removed Instruction #{i}")
                flag = True
                break
        if flag:
            continue
        user_input = input("Do you want to remove this instruction? (Y/N): ").strip().lower()
        if user_input == 'y':
            indices_to_remove.append(i)
            print(f"Removed Instruction #{i}")

# Remove the selected instructions from the updated data
updated_data = [item for i, item in enumerate(updated_data) if i not in indices_to_remove]

# Save the updated data to a new JSON file
with open('updated_data.json', 'w') as outfile:
    json.dump(updated_data, outfile, indent=2)

print("Original dataset preserved. Updated data saved as 'updated_data.json'.")