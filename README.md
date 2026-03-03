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
![Gráfico de Señales de Trading y Backtesting](https://github.com/albertogonzalezcord-del/Algorithmic-Trading-Crossover/blob/7e7d29b92e851eca4c072839dc5bb9841ed49a76/GOOG.PNG)
*(Gráfico generado por el script, tomando las acciones de GOOGLE como ejemplo, mostrando las entradas, salidas y la evolución del precio).*

# Limitaciones del Modelo 
Este proyecto es una primera aproximación al *algorithmic trading*. Como tal, soy consciente de las limitaciones intrínsecas de la estrategia actual: algunas, propias de las medias móviles simples, como podría ser que se otorga a todos los precios del periodo la misma ponderación, lo que es especialmente problemático en mercados laterales, y otras, derivadas de la simpleza del modelo, como es el haber ignorado las comisiones de los brokers al ejecutar cada entrada y salida, lo cual, lógicamente, distorionaría la hipotética rentabilidad final de haber seguido esta estrategia en la vida real.



