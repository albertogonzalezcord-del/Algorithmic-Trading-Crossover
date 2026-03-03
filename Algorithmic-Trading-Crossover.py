import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = input ("Ingrese el ticker: ").upper().strip()
print(f"Descargando datos de {ticker}...")

años = input("Ingrese el número de años de datos a analizar: ")
if años.isdigit():
    periodo = años + "y"
else:
    periodo = años

datos = yf.download (ticker, period = periodo)

if datos.empty:
    print(f"❌ Error: No se encontraron datos para '{ticker}'")
    exit() 

ticker_obj = yf.Ticker(ticker)
moneda = ticker_obj.info.get('currency', 'u.m.')
print(f"Moneda detectada: {moneda}")

ventana_rapida = 20
ventana_lenta = 50

datos['SMA_Rapida'] = datos['Close'].rolling(window=ventana_rapida).mean()
datos['SMA_Lenta'] = datos['Close'].rolling(window=ventana_lenta).mean()
datos = datos.dropna()
print("\nTabla con las Medias Móviles calculadas (últimos 5 días):")
print(datos[['Close', 'SMA_Rapida', 'SMA_Lenta']].tail())


datos['Posicion'] = (datos['SMA_Rapida'] > datos['SMA_Lenta']).astype(int)
datos['Señal'] = datos['Posicion'].diff()

dias_de_accion = datos[datos['Señal'] != 0].dropna()

print("\n--- REGISTRO DE SEÑALES DE TRADING ---")
print("1.0 = COMPRAR | -1.0 = VENDER")
print(dias_de_accion[['Close', 'SMA_Rapida', 'SMA_Lenta', 'Señal']])

plt.figure(figsize=(12, 6))
plt.plot(datos.index, datos['Close'], label='Precio de Cierre', color='orange', alpha=0.5)
plt.plot(datos.index, datos['SMA_Rapida'], label='Media Rápida (20 días)', color='blue', alpha=0.8)
plt.plot(datos.index, datos['SMA_Lenta'], label='Media Lenta (50 días)', color='purple', alpha=0.8)

dias_compra = datos[datos['Señal'] == 1.0]
plt.scatter(dias_compra.index, dias_compra['SMA_Rapida'], 
            marker='^', color='green', s=150, label='Comprar', zorder=5)

dias_venta = datos[datos['Señal'] == -1.0]
plt.scatter(dias_venta.index, dias_venta['SMA_Rapida'], 
            marker='v', color='red', s=150, label='Vender', zorder=5)

plt.title(f'Estrategia de Cruce de Medias Móviles - {ticker} ({periodo})')
plt.xlabel('Fecha')
plt.ylabel(f'Precio ({moneda})')
plt.legend() 
plt.grid(True, alpha=0.3) 
plt.show()

datos['Retorno_Mercado'] = datos['Close'].pct_change()
datos['Retorno_Estrategia'] = datos['Posicion'].shift(1) * datos['Retorno_Mercado']
datos['Dinero_Mercado'] = (1 + datos['Retorno_Mercado']).cumprod()
datos['Dinero_Estrategia'] = (1 + datos['Retorno_Estrategia']).cumprod()
resultado_mercado = (datos['Dinero_Mercado'].iloc[-1] - 1) * 100
resultado_estrategia = (datos['Dinero_Estrategia'].iloc[-1] - 1) * 100

print("\n" + "="*40)
print(f"   RESULTADOS DEL BACKTESTING ({años} AÑOS)")
print("="*40)
print(f"Ganancia por Comprar y Mantener (Buy & Hold) : {resultado_mercado:.2f}%")
print(f"Ganancia de la Estrategia: {resultado_estrategia:.2f}%")
print("="*40)
