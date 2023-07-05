# Balanceo de Carga usando Nginx

El enfoque de este trabajo de balanceo de datos con dos nodos consiste en implementar una aplicación en Flask que pueda sumar y restar dos números. Esta aplicación se ejecuta en un servidor Ubuntu 20.04 y se utiliza Nginx como balanceador de carga para distribuir las solicitudes entre los dos nodos.

## Desafios 

Los desafíos que pueden surgir al implementar este sistema incluyen:
- Configuración adecuada de Nginx para realizar el balanceo de carga de manera efectiva.
- Es importante asegurarse de que las solicitudes se distribuyan equitativamente entre los nodos y que el tráfico se maneje de manera eficiente.
- Garantizar que la comunicación entre los nodos y el balanceador de carga sea estable y confiable. Esto implica configurar correctamente la red e IP's y asegurarse de que los nodos estén sincronizados y actualizados con los cambios realizados en la aplicación.
- Manejo adecuado y correcto de el nombre del domino, ya que daba error, por lo que lo realicé solamente con con la IP local "Localhost"

## Hallazgos

También es importante monitorear y analizar el rendimiento del sistema para identificar posibles cuellos de botella o puntos de mejora. Esto puede incluir el uso de herramientas de monitoreo y análisis de rendimiento para obtener información sobre la carga de trabajo, los tiempos de respuesta y otros indicadores clave.
En general, este enfoque de balanceo de datos con dos nodos utilizando Flask, Ubuntu 20.04 y Nginx proporciona una solución escalable y confiable para la aplicación de sumar y restar números. La implementación adecuada y el monitoreo constante garantizan un rendimiento óptimo y una experiencia de usuario satisfactoria.

## Implementacion
Es importante recalcar que la implementación se da con python usando Flask, y en ambos nodos se logra identificar en cual de ellos se está al momento de ejecutar el balanceador.
- Aplicaciones
  
1:
  
![image](https://github.com/BradlhyMachado/BalanceoCargaNginx/assets/89551198/539790b7-7c87-4612-bbb3-f6a1be42ef28)

2:
  
![image](https://github.com/BradlhyMachado/BalanceoCargaNginx/assets/89551198/2292f540-2427-418c-90db-398e4065d0e3)

- Configurando Nginx:

![image](https://github.com/BradlhyMachado/BalanceoCargaNginx/assets/89551198/e292be14-4727-486b-85bd-b8f8785d7d51)



## Ejecución 
Para ejecutar la aplicación solo se levanta los servidores de la aplicación en ambos nodos
```bash
python3 app.py
```
![image](https://github.com/BradlhyMachado/BalanceoCargaNginx/assets/89551198/cab3b74e-8dd1-44d3-983e-01473d1ca4d1)

Además para probar el balanceador se ejecuta en el navegador web
![image](https://github.com/BradlhyMachado/BalanceoCargaNginx/assets/89551198/dcc0ba53-b23c-471e-be44-5be1ee85ac44)

