<img width="1149" height="545" alt="Comparison table of electrocardiogram (ECG) signal morphologies" src="https://github.com/user-attachments/assets/852f3422-7f72-4cef-921e-89a7ffb2677a" />
This is the zip file I used [mitbih_test.csv.zip](https://github.com/user-attachments/files/34027343/mitbih_test.csv.zip)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Customize the default size and style of charts for a polished look
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Read the CSV file without using the first row as a header, as the data consists purely of numbers
df = pd.read_csv('mitbih_test.csv.zip.csv', header=None)

# Check the data dimensions (number of rows, number of columns)
print("Data size:", df.shape)

# Display first 5 rows
display(df.head())

# Extract all rows labeled 0 (Normal) and 1 (Supraventricular)
normal_beats = df[df[187] == 0.0]
abnormal_beats = df[df[187] == 1.0]

# Extract the first row of data from each group, excluding the final label column ([:-1])
sample_normal = normal_beats.iloc[0, :-1]
sample_abnormal = abnormal_beats.iloc[0, :-1]

# Initialize canvas
plt.figure(figsize=(14, 6))

# Draw a normal signal line (in blue)
plt.plot(sample_normal, color='#2c3e50', linewidth=2, label="(Normal beats)")

# Draw the anomalous signal line (in red)
plt.plot(sample_abnormal, color='#e74c3c', linewidth=2, label="(Arrhythmia)")

# Add information for axes and titles
plt.title("Comparison table of electrocardiogram (ECG) signal morphologies", fontsize=16, fontweight='bold')
plt.xlabel("(Time Steps)", fontsize=12)
plt.ylabel("(Normalized Amplitude)", fontsize=12)

# Display captions
plt.legend(loc='upper right', fontsize=12)

# Export graph
plt.show()
