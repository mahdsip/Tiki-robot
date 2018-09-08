# Robot TIKI

Este proyecto contiene los fuentes necesarios para hacer funcionar un robot con una raspberry pi y un arduino capaz de recibir órdenes habladas para moverse así, como responder muchos tipos de preguntas bajo el projecto Jasper.

Se ha añadido el código a jasper.py para que al lanzar un error de aplicación llame al programa reloadTiki que lanzará una nueva instancia de jasper. Esto se hace porque de manera aleatoria cada x segundos se lanza una exepción y se para el servicio.

Los módulos de Jasper LEFT.py,RIGHT.py, GO.py y BACK.py lo que hacen es que si se menciona alguna de las cuatro palabras, se envía un número a arduino para que se mueva conforme a la orden recibida.

El código de main.c acepta un número por parámetro y envía dicho número por I2C al arduino. 

El código de arduino está esperando un número por interfaz I2C, dependiendo de lo que reciba mueve unos motores u otros. 

