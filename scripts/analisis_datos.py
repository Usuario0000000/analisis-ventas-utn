
# Análisis de Ventas 2025 - UTN Organización Empresarial
# Autor: Martín Milich

import pandas as pd
import matplotlib.pyplot as plt
import os

# Datos de ventas 2025 en pesos argentinos
data = {
    'mes': ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'],
    'producto': ['Laptop','Mouse','Teclado','Monitor','Laptop','Mouse',
                 'Teclado','Monitor','Laptop','Mouse','Laptop','Monitor'],
    'cantidad': [3,12,8,2,4,15,6,3,5,10,8,4],
    'precio':   [1800000,15000,25000,320000,1900000,16000,
                 26000,340000,2000000,17000,2100000,360000]
}

df = pd.DataFrame(data)
df['total'] = df['cantidad'] * df['precio']

print("Ventas totales 2025: $", df['total'].sum())
print("Producto mas vendido:", df.groupby('producto')['cantidad'].sum().idxmax())
print("Mes con mas ventas:", df.loc[df['total'].idxmax(), 'mes'])
print("Promedio mensual: $", round(df['total'].mean()))

df.plot(x='mes', y='total', kind='bar', legend=False, color='steelblue',
        title='Ventas Mensuales 2025')
plt.ylabel('Pesos argentinos')
plt.tight_layout()
os.makedirs('resultados', exist_ok=True)
plt.savefig('resultados/grafico_ventas.png')
print("Grafico guardado")
