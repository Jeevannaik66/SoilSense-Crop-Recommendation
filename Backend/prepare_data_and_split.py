import os
import shutil
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import numpy as np

# Step 1: Set Dataset Path
dataset_dir = 'C:/Users/Jeevan/Documents/Projects/SoilSense/Datasets/Soil Type'
processed_dir = 'C:/Users/Jeevan/Documents/Projects/SoilSense/Datasets/Processed'

train_dir = 'C:/Users/Jeevan/Documents/Projects/SoilSense/Datasets/Processed/Train'
val_dir = 'C:/Users/Jeevan/Documents/Projects/SoilSense/Datasets/Processed/Val'
test_dir = 'C:/Users/Jeevan/Documents/Projects/SoilSense/Datasets/Processed/Test'

# Step 2: Create Directories for Train, Validation, and Test Sets
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Step 3: Create Subdirectories for Each Soil Type
soil_types = os.listdir(dataset_dir)

for soil_type in soil_types:
    soil_type_path = os.path.join(dataset_dir, soil_type)
    if os.path.isdir(soil_type_path):  # Check if it is a directory (not a file)
        os.makedirs(os.path.join(train_dir, soil_type), exist_ok=True)
        os.makedirs(os.path.join(val_dir, soil_type), exist_ok=True)
        os.makedirs(os.path.join(test_dir, soil_type), exist_ok=True)

# Step 4: Perform Exploratory Data Analysis (EDA)
# Get the count of images per soil type
soil_counts = {soil: len(os.listdir(os.path.join(dataset_dir, soil))) for soil in soil_types if os.path.isdir(os.path.join(dataset_dir, soil))}
print("Class distribution:\n", soil_counts)

# Plot class distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=list(soil_counts.keys()), y=list(soil_counts.values()))
plt.xticks(rotation=90)
plt.xlabel('Soil Type')
plt.ylabel('Number of Images')
plt.title('Soil Type Image Distribution')
plt.show()

# Step 5: Split the Dataset into Train, Validation, and Test Sets (80%, 10%, 10%)
for soil_type in soil_types:
    soil_type_path = os.path.join(dataset_dir, soil_type)
    
    if os.path.isdir(soil_type_path):  # Only proceed if it's a directory
        image_names = os.listdir(soil_type_path)
        
        # Split images into train (80%), validation (10%), and test (10%)
        train_images, temp_images = train_test_split(image_names, test_size=0.2, random_state=42)  # 20% for validation and test
        val_images, test_images = train_test_split(temp_images, test_size=0.5, random_state=42)  # 50% of remaining 20% for validation and 50% for test
        
        # Move images to the corresponding folders
        for image_name in train_images:
            shutil.move(os.path.join(soil_type_path, image_name), os.path.join(train_dir, soil_type, image_name))
        for image_name in val_images:
            shutil.move(os.path.join(soil_type_path, image_name), os.path.join(val_dir, soil_type, image_name))
        for image_name in test_images:
            shutil.move(os.path.join(soil_type_path, image_name), os.path.join(test_dir, soil_type, image_name))

print("Dataset has been successfully split into Train (80%), Validation (10%), and Test (10%) sets.")

# Step 6: Check the Number of Images in Each Set
train_counts = {soil: len(os.listdir(os.path.join(train_dir, soil))) for soil in soil_types}
val_counts = {soil: len(os.listdir(os.path.join(val_dir, soil))) for soil in soil_types}
test_counts = {soil: len(os.listdir(os.path.join(test_dir, soil))) for soil in soil_types}

# Display the counts for each set
print(f"Training Set Distribution:\n {train_counts}")
print(f"Validation Set Distribution:\n {val_counts}")
print(f"Test Set Distribution:\n {test_counts}")

# Plot class distribution for Train, Validation, and Test sets
fig, axs = plt.subplots(1, 3, figsize=(15, 6))

# Training set distribution
axs[0].bar(train_counts.keys(), train_counts.values())
axs[0].set_title('Training Set Distribution ')
axs[0].set_xticklabels(train_counts.keys(), rotation=90)

# Validation set distribution
axs[1].bar(val_counts.keys(), val_counts.values())
axs[1].set_title('Validation Set Distribution')
axs[1].set_xticklabels(val_counts.keys(), rotation=90)

# Test set distribution
axs[2].bar(test_counts.keys(), test_counts.values())
axs[2].set_title('Test Set Distribution')
axs[2].set_xticklabels(test_counts.keys(), rotation=90)

plt.tight_layout()
plt.show()