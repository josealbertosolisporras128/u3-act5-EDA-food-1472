import pandas as pd
import matplotlib.pyplot as plt
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
print("\n--- grafica comida (x) tiempo de cocinado (y) ---")
print("\n--- grafica comida (x) texto a 30 grados ---")
nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title('comida tipica de india jose solis 1472')
plt.xlabel('nombre de platillo')
plt.ylabel('tiempo de cocinado')
plt.show()
plt.title('grafica de varias columnas jose solis 1472')
nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora .plot.bar(x='name', rot=30)
plt.title('grafica de 2 columnas jose solis 1472')
plt.xlabel('nombre de platillo')
plt.ylabel('tiempo de cocinado prep y comida')
plt.show()
print("----- graficas apiladas una tras otra verticalmente 1472 -----")
nombre_y_hora.plot.bar(x='name', stacked=True)
plt.title('grafica apilada jose solis 1472')
plt.xlabel('nombre de platillo')
plt.ylabel('tiempo de cocinado prep y comida')
plt.show()





