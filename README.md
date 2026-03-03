# Algorithmic-Trading-Crossover
Script en Python para identificar cambios de tendencia y generar señales de trading mediante el cruce de Medias Móviles (SMA)

# Funcionamiento
El programa pide al usuario un Ticker y un periodo de tiempo. Luego, de forma automática:
1. **Descarga el historial de precios** utilizando la API de Yahoo Finance: Yfinance.
2. **Calcula dos medias móviles:** Una rápida (20 días) y una lenta (50 días).
3. **Genera señales de trading:** Identifica las señales donde conviene Comprar (cruce alcista) o Vender (cruce bajista) según esta estrategia.
4. **Visualiza la estrategia:** Dibuja un gráfico interactivo mostrando el precio, las medias y marcadores (verde/rojo) para las operaciones.
5. **Realiza un Backtesting:** Compara el rendimiento del algoritmo frente a la estrategia de "Comprar y Mantener" (Buy & Hold).

# Tech Stack (Herramientas utilizadas)
* **Lenguaje principal:** Python 3
* **Manipulación de Datos:** `pandas`
* **Extracción Financiera:** `yfinance`
* **Visualización:** `matplotlib`

# Visualización de la Estrategia
