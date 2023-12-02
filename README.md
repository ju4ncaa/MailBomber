# MailStorm

<div align="center">
  <img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/5b6500eb-6ca4-4644-a6c2-9fb19bd811ae" width="170px">
</div>
<br>

Herramienta desarrollada en Python, que permite llevar a cabo ataques de email spamming de manera efectiva y sencilla. Este script utiliza el servicio de correo electrónico de Gmail para enviar múltiples correos electrónicos a una dirección de correo electrónico específica.

## Requisitos
Antes de ejecutar el script es crucial tener una "contraseña de aplicación" generada para tu cuenta de correo electrónico. Esto es necesario para permitir que el script envíe correos electrónicos en tu nombre sin comprometer la contraseña principal de tu cuenta.

### Pasos para Crear una Contraseña de Aplicación (Gmail)

1. **Inicia sesión en tu cuenta de Gmail:** Asegúrate de estar conectado a la cuenta desde la cual deseas enviar los correos electrónicos.

<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/d02cb09f-0042-4350-8884-da66ee4909d2" width="400px">

2. **Accede a la Configuración de Seguridad:** Ve a la configuración de seguridad de tu cuenta de Google. Puedes hacer esto desde [Configuración de cuenta de Google](https://myaccount.google.com/).

![imagen](https://github.com/0xJuaNc4/MailStorm/assets/130152767/833498eb-9604-4a26-b33f-b83046c1dee1)

3. **Habilita la Verificación en Dos Pasos:** Si no has habilitado la verificación en dos pasos, se te pedirá que lo hagas. Sigue las instrucciones para configurar este nivel adicional de seguridad.

<div align="center">
<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/b1ee1be6-f1d5-4484-84f0-60c0354cee32" width="650px">
</div>

4. **Genera la Contraseña de Aplicación:** En la sección de "Contraseñas de aplicaciones", elige "Seleccionar aplicación" y "Otro (nombre personalizado)". A continuación, haz clic en "Generar".

<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/eaeb45dc-dfe8-402d-b8b4-dc2353b34f66" width="500px">

 **Copia la Contraseña Generada:** Se te proporcionará una contraseña específica para la aplicación. Copia esta contraseña, ya que la necesitarás al ejecutar el script.

<img src="https://github.com/0xJuaNc4/MailStorm/assets/130152767/eb95df5e-93eb-4e78-96da-b17b60f0a902" width="500px">


## Uso

Clona el repositorio:
```
git clone https://github.com/tuusuario/MailStorm.git
```
Entra en el directorio del proyecto:
```
cd MailStorm
```
Ejecuta el script:
```
python mailstorm.py
```
