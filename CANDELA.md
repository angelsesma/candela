# Adquisición de Patrones y Análisis Comparativo en el Juego de Go: Un Enfoque Moderno  

**Autor:** Ángel Alberto Sesma González  
**Coautor:** Leonardo Jiménez Martínez  
**Fecha:** 14 de marzo de 2025  

---

## 1. Introducción  

El juego de Go representa un desafío significativo para la inteligencia artificial debido a su profunda complejidad, la cual ha cautivado a académicos durante siglos. Aunque los programas capaces de jugar Go existen desde hace décadas, los últimos nueve años (2016-2025) han marcado un punto de inflexión, con sistemas que alcanzan —e incluso superan— el rendimiento humano profesional. Un cambio notable en las estrategias de juego surgió alrededor de 2016, impulsado por la adopción de movimientos no convencionales pero efectivos demostrados por programas de IA, alterando fundamentalmente los enfoques tradicionales.  

Para investigar esta evolución, realizamos un estudio comparativo:  
Desarrollamos un programa en Python para analizar aproximadamente 3,000 partidas profesionales de los últimos cinco años, extendiendo el trabajo fundacional de Liu y Dou (2007) titulado *"Automatic Pattern Acquisition from Game Records in Go"* (publicado en *The Journal of China Universities of Posts and Telecommunications*). Su estudio pionero catalogó estadísticamente patrones en 9,500 partidas profesionales de principios de los 2000, sentando las bases para enfoques modernos basados en patrones en el Go computacional. Sin embargo, el panorama profesional del Go ha evolucionado significativamente desde entonces, con nuevas estrategias y estilos de juego emergentes.  

### Nuestras contribuciones son tres:  

1. Presentamos un algoritmo eficiente para la adquisición automática de patrones, basado en el trabajo de [1].  
2. Analizamos patrones de alta frecuencia en más de 3,000 partidas profesionales recientes, comparándolos con los resultados de 2007 para identificar tendencias evolutivas.  
3. Brindamos un análisis comparativo cuantitativo de patrones históricos y contemporáneos, revelando cambios en las estrategias del Go.  

---

## 2. Trabajo Relacionado  

La adquisición y análisis de patrones en el Go han sido ampliamente estudiados. Los primeros esfuerzos se centraron en la compilación manual de patrones y enfoques lingüísticos para nombrar movimientos específicos en relación con su entorno inmediato y formas resultantes (por ejemplo, *keima*, *hane*, *tsuke*, *shimari*, *kikashi*, *nobi*, *ikken-tobi*). En [1], se introdujo un método estadístico para la adquisición automática de patrones, definiéndolos como relaciones espaciales dentro de una cuadrícula fija de $5 \times 5$. Este trabajo demostró la viabilidad de extraer patrones de alta calidad de registros de partidas y enfatizó la importancia del uso estadístico para determinar la urgencia de un patrón.  

Los avances recientes en IA, particularmente el *aprendizaje por refuerzo profundo*, han desplazado el enfoque hacia sistemas como AlphaGo, KataGo o LeelaZero. No obstante, los enfoques basados en patrones siguen siendo relevantes para entender el juego humano y desarrollar sistemas de IA. Estudios desde los años 90 han explorado la *búsqueda en árbol Monte Carlo* para generación de movimientos [2], terminología para situaciones en el tablero (por ejemplo, libertades, capturas, *ko fights* y grupos vivos) [3, 4], métodos combinatorios para resolver posiciones complejas en el final del juego [5], y niveles de complejidad catalogados para reglas y variantes del Go [6].  

A pesar de estos avances, existe una falta de estudios comparativos que analicen la evolución de los patrones del Go a lo largo del tiempo. Este artículo aborda esa brecha aplicando la metodología de [1] a un conjunto de datos moderno de partidas profesionales.  

---

## 3. Metodología  

### 3.1 Definición de Patrón  

Un patrón de Go se define como una configuración espacial de piedras dentro de una cuadrícula de $5 \times 5$ centrada en un movimiento dado [1]. Nuestro objetivo principal fue construir una base de datos de patrones de $5 \times 5$, extraídos sistemáticamente de cada movimiento en cada partida, y cuantificar sus frecuencias. Para garantizar precisión, implementamos una función de representación canónica que agrupa patrones equivalentes considerando rotaciones, reflexiones e inversiones de color. Este método elimina redundancias, permitiendo comparaciones estadísticas precisas entre épocas.  

Adicionalmente, implementamos una función para distinguir patrones en las tres líneas exteriores del tablero de aquellos más alejados de los bordes. Esto es crítico para patrones urgentes, que a menudo se relacionan con movimientos de apertura y estrategias iniciales.  

### 3.2 Conjunto de Datos  

Recopilamos 3,147 partidas profesionales recientes de repositorios en línea (por ejemplo, [http://go4go.net](http://go4go.net)). Los registros se descargaron automáticamente usando un programa diseñado por el Dr. Mario Alberto Mercado para cálculos de energía hamiltoniana, y compartido con el autor principal como parte de un proyecto colaborativo.  

### 3.3 Algoritmo de Adquisición de Patrones  

Basándonos en el pseudocódigo de [1], implementamos el algoritmo en Python 3. En esta versión, solo se extraen los 16 patrones más frecuentes para simplificar el análisis comparativo:  

```python  
Para cada partida:  
    Para cada movimiento:  
        Extraer la cuadrícula 5×5 centrada en el movimiento.  
        Convertir la cuadrícula a su forma canónica.  
        Actualizar la frecuencia del patrón en la base de datos.  
Ordenar la base de datos en orden descendente.  
Imprimir los 16 patrones principales con su frecuencia.
```

### 3.4 Análisis Estadístico  

Analizamos la distribución de frecuencias de los patrones e identificamos los 16 más frecuentes. Con base en estos resultados, detectamos posibles cambios estilísticos en el juego profesional durante 18 años.  

---

## 4. Resultados  

### 4.1 Patrones de Alta Frecuencia  

- La invasión *san-san* (punto 3-3) ascendió del 13° al 4° lugar en frecuencia.  
- El *shimari* (cerco en la esquina) cayó del 6° al 9° lugar.  
- El *hane* contra una piedra aislada disminuyó del 9° al 11° lugar.  

![Patrones principales en partidas profesionales (Sesma y Jiménez, 2025)](figure1.png)  
*Figura 1: Patrones principales en partidas profesionales (Sesma y Jiménez, 2025).*  

![Patrones principales en partidas profesionales (Liu y Dou, 2007)](figure2.png)  
*Figura 2: Patrones principales en partidas profesionales (Liu y Dou, 2007).*  

### 4.2 Evolución de Estrategias  

La invasión 3-3, antes considerada una táctica de final de juego, ha ganado urgencia, mientras que el *shimari* clásico ha perdido prominencia, reflejando una tendencia hacia un juego agresivo y proactivo.  

El punto de apertura 4-4, históricamente secundario, ahora domina sobre el 3-4, mostrando preferencias modernas por aperturas flexibles y equilibradas.  

---

## 5. Discusión  

Si bien el análisis regional de $5 \times 5$ no captura dinámicas globales, revela patrones de baja frecuencia que sirven como continuaciones de los de alta frecuencia. Al comparar la prevalencia de un patrón con sus continuaciones locales, inferimos la frecuencia relativa de movimientos fuera del área de $5 \times 5$ —un fenómeno consistente con *tennuki* (priorizar un movimiento distante sobre una continuación local). Por ejemplo, si un patrón excede la frecuencia de su continuación inmediata, es probable que los jugadores prioricen estrategias globales sobre batallas locales.  

Los avances en potencia computacional permiten expandir esta metodología a regiones más grandes (por ejemplo, $7 \times 7$ o $9 \times 9$), ofreciendo *insights* más ricos sobre la evolución estratégica. La replicación periódica de este estudio podría profundizar la comprensión del juego profesional, revitalizar proverbios tradicionales y modernizar marcos pedagógicos.  

---

## 6. Conclusión  

Este artículo presenta un enfoque moderno para la adquisición automática de patrones en el Go, basado en el trabajo fundacional de [1]. Al analizar un extenso conjunto de datos de partidas profesionales recientes, identificamos tendencias clave en el uso de patrones, ofreciendo nuevas perspectivas sobre la evolución estratégica. Nuestros resultados subrayan la relevancia de los enfoques basados en patrones tanto en el juego humano como en la IA, y brindan un marco para futuras investigaciones en IA de juegos y reconocimiento de patrones.  

---

## 7. Agradecimientos  

Agradecemos al asistente virtual Deepseek por sus capacidades multidisciplinarias y por refinar este trabajo para su presentación en inglés.  

Agradecemos a Mario Alberto Mercado y Siddartha Ávila por su apoyo durante este estudio.  

Por último, dedicamos este trabajo a la memoria del Profesor José "Pepe Chac" Chacón, por su ejemplar espíritu de lucha y contribuciones invaluables a la comunidad mexicana de Go.  

---

## 8. Referencias  

1. Liu, Z., & Dou, Q. (2007). Automatic pattern acquisition from game records in Go. *The Journal of China Universities of Posts and Telecommunications, 14*(1), 100-106.  
2. Bouzy, B., & Cazenave, T. (2001). Computer go: An AI oriented survey. *Journal of Artificial Intelligence, 132*(1), 39-103.  
3. Yee, A., & Alvarado, M. (2015). Mathematical modeling and analysis of learning techniques for the game of Go. *International Journal of Mathematical Models and Methods in Applied Sciences, 9*(1), 293-302.  
4. Spight, W. (2001). Extended thermography for multiple kos in Go. *Theoretical Computer Science, 252*(1), 23-43.  
5. Berlekamp, E., & Wolfe, D. (1994). *Mathematical Go: Chilling Gets the Last Point*. A. K. Peters.  
6. Saffidine, A., Teytaud, O., & Yen, S.-J. (2015). Go complexities. *Proceedings of the Advances in Computer Games Conference* (pp. 8899). Springer.  

--- 
