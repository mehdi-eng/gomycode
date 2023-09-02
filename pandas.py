import pandas as pd
import numpy as np

# Create the initial DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

# Print the first three rows using head()
print("First three rows:")
print(df.head(3))

# Delete rows with NaN values
df.dropna(inplace=True)

# Extract 'name' and 'score' columns
name_score_df = df[['name', 'score']]

# Append a new row 'k' to the DataFrame
new_row = pd.Series({'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}, name='k')
df = df.append(new_row)

# Delete the 'attempts' column
df.drop('attempts', axis=1, inplace=True)

# Add a new 'Success' column
df['Success'] = (df['score'] > 10).astype(int)

# Export the final DataFrame to a CSV file
df.to_csv('my_data.csv')

# Print the final DataFrame
print("\nFinal DataFrame:")
print(df)
