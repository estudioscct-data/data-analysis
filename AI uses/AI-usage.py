import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
ruta = 'C:/Users/HP/Desktop/Proyectos/data-analysis/AI uses/students_ai_usage.csv'
data = pd.read_csv(ruta)
print(data.head())      
max_age = data['age'].max()
print(f'La edad máxima de los estudiantes es: {max_age}')
