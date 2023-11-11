import pandas as pd

# Create a pandas DataFrame from the JSON data
read_content = pd.read_json('new_tasks/regen3.json')
df = pd.DataFrame(read_content)

# Create an Excel writer
excel_writer = pd.ExcelWriter("new_seeds.xlsx", engine="xlsxwriter")

# Write the DataFrame to the Excel file
df.to_excel(excel_writer, sheet_name="Sheet1", index=False)

# Get the xlsxwriter workbook and worksheet objects
workbook = excel_writer.book
worksheet = excel_writer.sheets["Sheet1"]

# Add a header row with "instruction," "input," and "output" as column names
header_format = workbook.add_format({'bold': True, 'text_wrap': True})
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

# Set column widths based on content
for i, col in enumerate(df.columns):
    max_len = max(df[col].astype(str).str.len().max(), len(col))
    worksheet.set_column(i, i, max_len)

# Save the Excel file
excel_writer._save()
