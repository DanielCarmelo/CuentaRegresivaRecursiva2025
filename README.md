Este programa le pide al usuario que ingrese un número entero positivo. Si el número es negativo, lo convierte en positivo para que siempre funcione bien. Después, comienza una cuenta regresiva desde ese número hasta el cero.

Para cada número en la cuenta regresiva, el programa dice si ese número es par o impar. Al terminar, cuando llega a cero, muestra un mensaje especial que dice que la cuenta regresiva terminó.

Así, el programa ayuda a practicar la cuenta regresiva y a identificar números pares e impares, todo de forma automática y fácil de entender

La función es_par_o_impar recibe un número y me dice si ese número es par o impar. Para eso, usa el operador % que calcula el resto de la división por 2. Si el resto es cero, significa que el número es par; si no, es impar. Entonces devuelve una frase que dice el número junto con si es “par” o “impar”.

La función cuenta_regresiva hace una cuenta regresiva desde un número que le doy hasta cero. Para eso usa un bucle for que va bajando de uno en uno desde el número hasta cero. En cada número que pasa, usa la función es_par_o_impar para imprimir el número y decir si es par o impar.

Así, el programa me muestra todos los números desde el que elegí hasta cero y me dice si cada uno es par o impar.
