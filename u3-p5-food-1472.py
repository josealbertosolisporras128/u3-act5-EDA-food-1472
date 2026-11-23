import pandas as pd
import matplotlib as plt
# jose solis nc 1472
# 1. Leer el archivo CSV comida pais india
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV comida india 1472 ---")
print(df_food_india)
print("\n--- mostrar nombre comida + ingredientes 1472 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- tiempo de cocción mostrar 10 registros con head 1472 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)















