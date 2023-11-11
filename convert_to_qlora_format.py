import pandas as pd

data = pd.read_json('updated_data.json')
df = pd.DataFrame(data)

df['text'] = "###Human: " + df['instruction'] + " ###Assistant: " + df['output']
df = df.drop(columns=['instruction', 'input', 'output'])
df.to_excel('updated_qlora_input.xlsx', index=False)

print("Excel file 'updated_qlora_input.xlsx' ban gya bhai! :D")