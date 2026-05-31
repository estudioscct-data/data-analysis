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
# the students who use IA improve their grades?
data_ia = data[data['uses_ai'] == 'Yes'].copy()[['grades_before_ai', 'grades_after_ai', 'purpose_of_ai', 'ai_tools_used']]
data_ia['improvement'] = data_ia['grades_after_ai'] - data_ia['grades_before_ai']
print(data_ia[['grades_before_ai', 'grades_after_ai', 'improvement']].head())
mean_improvement = data_ia['improvement'].mean()
print(f'Promedio de mejora en calificaciones: {mean_improvement:.2f}')
print(f"Mediana de la mejora: {data_ia['improvement'].median():.2f} puntos")
plt.hist(data_ia['improvement'], bins=10, edgecolor='black')
plt.title('Distribución de la mejora en notas (después - antes)')
plt.xlabel('Diferencia en puntos')
plt.ylabel('Cantidad de estudiantes')
plt.axvline(x=0, color='red', linestyle='--', label='Sin cambio')
plt.legend()
plt.show()
#the purpose of using IA and their improvements are related?

improve_purpose = data_ia.groupby('purpose_of_ai')['improvement'].mean().reset_index()
improve_purpose.plot(kind='barh', x='purpose_of_ai', y='improvement', legend=False, color='teal', edgecolor='black')
plt.title('Mejora promedio en notas según propósito de uso de IA')
plt.xlabel('Mejora en puntos (después - antes)')
plt.ylabel('Propósito')
plt.axvline(x=0, color='red', linestyle='--')
plt.show()

#which AI tools are more used by students? and which one is the most effective in improving their grades?
most_popular = data_ia['ai_tools_used'].value_counts()
print("Herramientas de IA más utilizadas por los estudiantes:")
print(most_popular)
most_popular.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Herramientas de IA más utilizadas por los estudiantes')
plt.xlabel('Herramienta de IA')
plt.ylabel('Cantidad de estudiantes')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)   
plt.show()

most_effective = data_ia.groupby('ai_tools_used')['improvement'].mean().reset_index()
most_effective = most_effective.sort_values(by='improvement', ascending=False)
most_effective.plot(kind='barh', x='ai_tools_used', y='improvement', legend=False, color='coral', edgecolor='black')
plt.title('Mejora promedio en notas según herramienta de IA utilizada')
plt.xlabel('Mejora en puntos (después - antes)')
plt.ylabel('Herramienta de IA')
plt.axvline(x=0, color='red', linestyle='--')
plt.show()