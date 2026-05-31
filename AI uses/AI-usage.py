import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = 'C:/Users/HP/Desktop/Proyectos/data-analysis/AI uses/students_ai_usage.csv'
data = pd.read_csv(file_path)

# Display first rows
print("First 5 rows of the dataset:")
print(data.head())

# Age range
max_age = data['age'].max()
min_age = data['age'].min()
print(f"Maximum student age: {max_age}")
print(f"Minimum student age: {min_age}")

# Question 1: Do younger students use AI more?
proportion = data.groupby('age')['uses_ai'].value_counts(normalize=True).unstack()
percentage = proportion * 100
print("\nPercentage of AI usage by age:")
print(percentage)

# Plot: AI usage by age (only 'Yes')
percentage_yes = percentage.loc[:, 'Yes']
percentage_yes.plot(kind='bar')
plt.title('AI Usage by Age', fontsize=14)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xlabel('Age', fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Question 2: Screen time comparison (AI users vs non-AI users)
screen_time_ai_users = data[data['uses_ai'] == 'Yes']['daily_screen_time_hours']
screen_time_non_ai_users = data[data['uses_ai'] == 'No']['daily_screen_time_hours']

mean_screen_time_ai = screen_time_ai_users.mean()
mean_screen_time_non_ai = screen_time_non_ai_users.mean()

print(f"\nAverage screen time for AI users: {mean_screen_time_ai:.2f} hours")
print(f"Average screen time for non-AI users: {mean_screen_time_non_ai:.2f} hours")

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='uses_ai', y='daily_screen_time_hours', data=data)
plt.title('Screen Time by AI Usage', fontsize=14)
plt.xlabel('Uses AI', fontsize=12)
plt.ylabel('Daily Screen Time (hours)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Barplot with averages
plt.figure(figsize=(8, 6))
sns.barplot(x='uses_ai', y='daily_screen_time_hours', data=data, estimator='mean', errorbar='sd')
plt.title('Average Screen Time by AI Usage', fontsize=14)
plt.xlabel('Uses AI', fontsize=12)
plt.ylabel('Average Daily Screen Time (hours)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Question 3: Do AI users improve their grades?
data_ia = data[data['uses_ai'] == 'Yes'].copy()[['grades_before_ai', 'grades_after_ai', 'purpose_of_ai', 'ai_tools_used']]
data_ia['improvement'] = data_ia['grades_after_ai'] - data_ia['grades_before_ai']

print("\nFirst rows of improvement data:")
print(data_ia[['grades_before_ai', 'grades_after_ai', 'improvement']].head())

mean_improvement = data_ia['improvement'].mean()
median_improvement = data_ia['improvement'].median()

print(f"Average grade improvement: {mean_improvement:.2f} points")
print(f"Median grade improvement: {median_improvement:.2f} points")

# Histogram of improvement
plt.hist(data_ia['improvement'], bins=10, edgecolor='black')
plt.title('Distribution of Grade Improvement (After - Before)', fontsize=14)
plt.xlabel('Grade Difference (points)', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.axvline(x=0, color='red', linestyle='--', label='No change')
plt.legend()
plt.show()

# Question 4: Improvement by purpose of AI usage
improve_purpose = data_ia.groupby('purpose_of_ai')['improvement'].mean().reset_index()
improve_purpose = improve_purpose.sort_values(by='improvement', ascending=True)  # Sorted for better readability

improve_purpose.plot(kind='barh', x='purpose_of_ai', y='improvement', legend=False, color='teal', edgecolor='black')
plt.title('Average Grade Improvement by Purpose of AI Usage', fontsize=14)
plt.xlabel('Grade Improvement (points)', fontsize=12)
plt.ylabel('Purpose of AI', fontsize=12)
plt.axvline(x=0, color='red', linestyle='--')
plt.tight_layout()
plt.show()

# Question 5: Most used AI tools and their effectiveness
most_popular = data_ia['ai_tools_used'].value_counts()
print("\nMost used AI tools:")
print(most_popular)

most_popular.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Most Used AI Tools by Students', fontsize=14)
plt.xlabel('AI Tool', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Effectiveness by AI tool
most_effective = data_ia.groupby('ai_tools_used')['improvement'].mean().reset_index()
most_effective = most_effective.sort_values(by='improvement', ascending=False)

print("\nAverage grade improvement by AI tool:")
print(most_effective)

most_effective.plot(kind='barh', x='ai_tools_used', y='improvement', legend=False, color='coral', edgecolor='black')
plt.title('Average Grade Improvement by AI Tool', fontsize=14)
plt.xlabel('Grade Improvement (points)', fontsize=12)
plt.ylabel('AI Tool', fontsize=12)
plt.axvline(x=0, color='red', linestyle='--')
plt.tight_layout()
plt.show()