import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (header=None since MIT-BIH CSVs typically lack column names)
df = pd.read_csv('mitbih_test.csv.zip', header=None)

# Dictionary mapping the classification label (column 187) to its descriptive name
label_names = {
    0.0: 'Normal beat (N)',
    1.0: 'Supraventricular premature beat (S)',
    2.0: 'Premature ventricular contraction (V)',
    3.0: 'Fusion of ventricular and normal beat (F)',
    4.0: 'Unclassifiable beat (Q)'
}

# Initialize a figure with 5 vertical subplots
# sharex and sharey ensure the time and amplitude axes are synchronized across all graphs
fig, axes = plt.subplots(5, 1, figsize=(10, 12), sharex=True, sharey=True)

# Loop through the 5 target classes (0 to 4)
for i in range(5):
    # Filter the dataframe for rows where the last column (label) matches the current class 'i'
    class_data = df[df.iloc[:, -1] == i]
    
    if not class_data.empty:
        # Extract the very first heartbeat sample for this class, excluding the label column ([:-1])
        sample = class_data.iloc[0, :-1]
        
        # Select the corresponding subplot and plot the signal array
        ax = axes[i]
        ax.plot(sample.values, color='#1f77b4', linewidth=2)
        
        # Formatting the subplot
        ax.set_title(f"{label_names[i]}", fontsize=12, fontweight='bold')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_ylabel("Normalized\nAmplitude", fontsize=10)

# Apply the x-axis label only to the bottom subplot to keep it clean
axes[-1].set_xlabel("Time (Samples)", fontsize=12)

# Add a main title to the entire figure
plt.suptitle("Comparison of ECG Signal Morphologies (MIT-BIH)", fontsize=16, y=1.02)

# Adjust spacing to prevent overlapping text
plt.tight_layout()

# Display the final visualization
plt.show()