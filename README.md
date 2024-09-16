# Trabajo Práctico N° 14 - Algoritmos de Ordenamiento

## Algoritmos de Ordenamiento Implementados

### 1. Ordenamiento Burbuja (Bubble Sort)
- **Descripción**: El algoritmo de burbuja compara pares adyacentes de elementos y los intercambia si están en el orden incorrecto. Se repite este proceso varias veces hasta que la lista esté ordenada.
- **Complejidad**: O(n²) en el peor y promedio de los casos.
- **Ventajas**: Fácil de entender e implementar.
- **Desventajas**: No es eficiente para listas grandes debido a su alta complejidad temporal.

### 2. Ordenamiento por Selección (Selection Sort)
- **Descripción**: El algoritmo selecciona el elemento más pequeño de la lista no ordenada y lo coloca en la posición adecuada. Este proceso se repite hasta que la lista está completamente ordenada.
- **Complejidad**: O(n²) en todos los casos.
- **Ventajas**: Realiza menos intercambios que el ordenamiento burbuja.
- **Desventajas**: Similarmente ineficiente para listas grandes.

### 3. Ordenamiento por Inserción (Insertion Sort)
- **Descripción**: El algoritmo toma elementos de la lista uno a uno y los inserta en su posición correcta en una lista ordenada parcial. Este proceso se repite hasta que toda la lista está ordenada.
- **Complejidad**: O(n²) en el peor caso, O(n) en el mejor caso (cuando la lista ya está casi ordenada).
- **Ventajas**: Muy eficiente para listas pequeñas o listas que ya están casi ordenadas.
- **Desventajas**: No es adecuado para listas grandes.

### 4. Ordenamiento Rápido (QuickSort)
- **Descripción**: QuickSort es un algoritmo de dividir y conquistar. Selecciona un pivote, reorganiza la lista de manera que todos los elementos menores al pivote queden a su izquierda y los mayores a su derecha, y luego ordena recursivamente las sublistas.
- **Complejidad**: O(n log n) en promedio, O(n²) en el peor caso.
- **Ventajas**: Es muy eficiente en la mayoría de los casos.
- **Desventajas**: Su eficiencia puede verse afectada si el pivote no se elige adecuadamente.

### 5. Ordenamiento por Fusión (MergeSort)
- **Descripción**: MergeSort también sigue el principio de dividir y conquistar. Divide la lista en mitades, las ordena recursivamente, y luego las combina de manera que queden ordenadas.
- **Complejidad**: O(n log n) en todos los casos.
- **Ventajas**: Es eficiente y tiene un buen rendimiento garantizado en todos los casos.
- **Desventajas**: Requiere espacio adicional para combinar las listas divididas.

## Conclusión General
Los algoritmos de ordenamiento tienen distintas fortalezas y debilidades según el caso de uso. Para listas pequeñas o casi ordenadas, el ordenamiento por inserción es más eficiente. Para grandes volúmenes de datos, algoritmos como QuickSort y MergeSort son las opciones más adecuadas.
