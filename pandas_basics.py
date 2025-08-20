import pandas as pd

# Create a small dataset (like a CSV file)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 95]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("📊 Student Data:")
print(df)

# Show basic info
print("\n🔹 DataFrame Info:")
print(df.info())

# Select a single column
print("\n🎯 Marks Column:")
print(df["Marks"])

# Calculate average marks
print("\n📈 Average Marks:", df["Marks"].mean())

# Filter students with marks > 85
print("\n🏆 Students with marks > 85:")
print(df[df["Marks"] > 85])
