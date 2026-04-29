# Métodos — Errores de Programación

## 1. Error de Redondeo Binario
Ocurre cuando un número decimal no tiene representación exacta en binario
y la computadora lo aproxima al valor más cercano representable.

**Ejemplo 1 — Situación resuelta:**
Una tienda calcula el precio final de 3 productos a $0.10 cada uno.
Se esperaría $0.30 pero la computadora arroja $0.30000000000000004
debido al redondeo binario. Se resuelve redondeando el resultado final
a 2 decimales con la función round().

**Ejemplo 2 — Situación resuelta:**
Un sensor industrial mide temperaturas en decimales. Al acumular
lecturas de 0.1°C en un ciclo de 10 iteraciones se obtiene
0.9999999999999999 en lugar de 1.0. Se resuelve usando la función
round() al momento de mostrar el resultado.

**Ejemplo 3 — Situación no resuelta:**
Un sistema bancario suma miles de transacciones de $0.01 sin aplicar
redondeo. El error acumulado genera diferencias de centavos en el
balance final que no se detectan hasta una auditoría.

---

## 2. Pérdida de Precisión por Magnitud (IEEE 754)
Ocurre cuando se opera con números de magnitudes muy diferentes.
El número pequeño pierde sus dígitos significativos al alinearse
con el grande en la representación IEEE 754.

**Ejemplo 1 — Situación resuelta:**
Un satélite calcula su posición sumando una corrección de 0.000001 km
a una distancia de 1,000,000 km. Se resuelve usando tipos de dato
de doble precisión (float64) para preservar los dígitos del número pequeño.

**Ejemplo 2 — Situación resuelta:**
Un microscopio electrónico mide desplazamientos de 0.0000001 mm
sobre una base de 100 mm. Se resuelve escalando las unidades
para trabajar con números de magnitud similar.

**Ejemplo 3 — Situación no resuelta:**
Un sistema de navegación aérea suma altitudes en metros con
correcciones en milímetros sin ajuste de escala. La corrección
desaparece completamente y el avión no ajusta su trayectoria.

---

## 3. Comparación Directa con ==
Comparar dos números flotantes con == casi siempre falla porque
la representación binaria introduce pequeñas diferencias.

**Ejemplo 1 — Situación resuelta:**
Un cajero automático verifica si el saldo es exactamente $100.00
usando ==. Falla por redondeo. Se resuelve comparando si la
diferencia absoluta entre ambos valores es menor a 0.001.

**Ejemplo 2 — Situación resuelta:**
Un videojuego detecta si un proyectil llegó exactamente a su destino
comparando coordenadas flotantes con ==. Se resuelve usando un margen
de tolerancia (epsilon) en la comparación.

**Ejemplo 3 — Situación no resuelta:**
Un sistema de control de una válvula industrial verifica con ==
si la presión llegó al valor exacto de apertura. La válvula nunca
abre porque el valor exacto nunca se alcanza por redondeo.

---

## 4. Acumulación de Errores en Bucles
Cada iteración introduce un pequeño error de redondeo que se
suma a los anteriores, generando un error total significativo
al final del ciclo.

**Ejemplo 1 — Situación resuelta:**
Una simulación física suma 0.1 segundos en cada iteración durante
1000 pasos. El tiempo acumulado tiene error. Se resuelve multiplicando
el paso de tiempo por el número de iteración en lugar de ir sumando.

**Ejemplo 2 — Situación resuelta:**
Un contador de distancia en un robot suma pequeños desplazamientos
en cada ciclo. Se resuelve reiniciando el acumulador periódicamente
y usando un valor de referencia externo.

**Ejemplo 3 — Situación no resuelta:**
Un sistema de navegación de un submarino acumula errores de posición
durante 72 horas sin corrección externa. Al final la posición
calculada difiere varios kilómetros de la real.

---

## 5. Cancelación por Resta (Loss of Significance)
Al restar dos números casi iguales, los dígitos significativos
se cancelan y el resultado pierde precisión.

**Ejemplo 1 — Situación resuelta:**
Una fórmula química calcula la diferencia de concentraciones
entre 1.0000001 y 1.0000000. Se resuelve reordenando
algebraicamente la fórmula para evitar la resta directa.

**Ejemplo 2 — Situación resuelta:**
Un sistema financiero calcula la variación diaria de un índice
bursátil entre valores casi idénticos. Se resuelve trabajando
directamente con el porcentaje de cambio en lugar de la resta.

**Ejemplo 3 — Situación no resuelta:**
Una central nuclear calcula la diferencia de temperaturas entre
dos sensores casi iguales usando resta directa. El resultado
es tan impreciso que el sistema de enfriamiento no responde
a tiempo.

---

## 6. Desbordamiento Silencioso (Overflow)
Ocurre cuando el resultado de una operación supera el valor
máximo representable por el tipo de dato y se convierte en
un valor incorrecto sin avisar.

**Ejemplo 1 — Situación resuelta:**
Un sistema de puntuación de videojuego usa entero de 16 bits.
Al superar 32,767 puntos el marcador se vuelve negativo.
Se resuelve cambiando a entero de 32 o 64 bits.

**Ejemplo 2 — Situación resuelta:**
Una aplicación de astronomía calcula distancias en metros entre
galaxias. El número supera el límite del tipo de dato.
Se resuelve usando notación científica con punto flotante de 64 bits.

**Ejemplo 3 — Situación no resuelta:**
El cohete Ariane 5 en 1996 convirtió un número de 64 bits a
16 bits sin verificar el rango. El desbordamiento causó un
fallo del sistema de navegación y la explosión del cohete
a los 37 segundos de vuelo.

---

## 7. Conversión Estrecha (Narrowing Primitive Conversion)
Ocurre cuando se convierte un tipo de dato de mayor precisión
a uno de menor precisión, perdiendo información sin advertencia.

**Ejemplo 1 — Situación resuelta:**
Un sistema médico convierte temperaturas de double a int para
mostrarlas en pantalla. Se pierde el decimal. Se resuelve
usando round() antes de convertir y mostrando siempre con decimal.

**Ejemplo 2 — Situación resuelta:**
Un sensor de velocidad registra 99.9 km/h como double y lo
convierte a int resultando en 99. Se resuelve usando Math.round()
para redondear correctamente antes de la conversión.

**Ejemplo 3 — Situación no resuelta:**
Un sistema de dosificación de medicamentos convierte la dosis
calculada de double a int truncando el decimal. Un paciente
recibe menos medicamento del necesario durante semanas sin
que nadie lo detecte.