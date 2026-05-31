import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
ruta = 'C:/Users/HP/Desktop/Proyectos/data-analysis/AI uses/students_ai_usage.csv'
data = pd.read_csv(ruta)
print(data.head())      
max_age = data['age'].max()
min_age = data['age'].min()
print(f'La edad máxima de los estudiantes es: {max_age}')
print(f'La edad minima de los estudiantes es: {min_age}')
# the most youngest use mor IA than older students?
data.loc[:,['age', 'uses_ai']]
proportion = data.groupby('age')['uses_ai'].value_counts(normalize = True).unstack()
porcentual = proportion * 100
print(porcentual)
proportion_yes = porcentual.loc[:, 'Yes']
proportion_yes.plot(kind='bar')
plt.title('Uso de IA por edad', fontsize=14)
plt.ylabel('Porcentaje (%)', fontsize=12)
plt.xlabel('Edad', fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# the students who use IA, how many hours do they spend on the screen? they spend
# more time on the screen than those who do not use IA? 
screen_time_ai_users = data[data['uses_ai'] == 'Yes']['daily_screen_time_hours']
screen_time_non_ai_users = data[data['uses_ai'] == 'No']['daily_screen_time_hours']
mean_screen_time_ai_users = screen_time_ai_users.mean()
mean_screen_time_non_ai_users = screen_time_non_ai_users.mean()
print(f'Tiempo promedio en pantalla para usuarios de IA: {mean_screen_time_ai_users:.2f} horas')
print(f'Tiempo promedio en pantalla para no usuarios de IA: {mean_screen_time_non_ai_users:.2f} horas')
plt.figure(figsize=(10, 6))
sns.boxplot(x='uses_ai', y='daily_screen_time_hours', data=data)
plt.title('Tiempo en pantalla por uso de IA', fontsize=14)
plt.xlabel('Uso de IA', fontsize=12)
plt.ylabel('Horas diarias en pantalla', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
promedio_screen_time = data.groupby('uses_ai')['daily_screen_time_hours'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='uses_ai', y='daily_screen_time_hours', data=data, estimator='mean', errorbar='sd')
plt.title('Tiempo promedio en pantalla por uso de IA', fontsize=14)
plt.xlabel('Uso de IA', fontsize=12)
plt.ylabel('Horas diarias en pantalla (promedio)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
#the students who use IA improve their grades?