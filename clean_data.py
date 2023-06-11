import pandas as pd

# CSV input file path
input_file = 'input_file.csv'

# CSV output file path
output_file = 'output_file.csv'

# CSV file into a DataFrame
df = pd.read_csv(input_file)

# Columns_to_delete
columns_to_delete = ['AuthorID', 'Attachments','Reactions']

# Delete columns
df = df.drop(columns=columns_to_delete)

# Rename authors to their real names
df['Author'] = df['Author'].replace({'User#1234': 'Carlos', 'user1#2345': 'Juan'})


# Save DataFrame to CSV
df.to_csv(output_file, index=False)