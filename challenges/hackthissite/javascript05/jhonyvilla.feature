#language: es

  Característica: Resolver reto Javascript 5
    Del sitio hackthissite.org
    Con mi usuario LordJhony

  Antecedentes:
    Dado que estoy registrado en el sitio hackthissite.org
    Y tengo el sistema operativo Windows en su versión 7
    Y tengo acceso a internet

  Escenario: Solución exitosa
    Dada una pagina web se pide encontrar una contraseña
    Y esa contraseña se comprueba con una función en javascript
    Cuando examino el codigo fuente
    Y encuentro la función
    Y la función tiene la contraseña encriptada en hexadecimal
    Y desencripto la clave
    Entonces resuelvo el reto
