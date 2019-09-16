# sms-twilio-django
Para comenzar a usar Twilio, tendremos que obtener un número de Twilio. Tendremos que registrarnos, registrarnos [aquí](https://www.twilio.com/try-twilio).

Twilio le pedirá su número y le enviará un código para su verificación. Marque la opción si no desea que Twilio se comunique con usted en su número. Entonces, hecho!

Twilio le proporcionará uno predeterminado y tendrá la opción de aceptarlo o buscar otro.

### Usaremos un nuevo directorio en tu directorio home:
    $ mkdir nombre_directorio
    $ cd nombre_directorio

### Entorno virtual

Haremos un virtualenv llamado smstwilio. El comando general estará en el formato:

    $ python3 -m venv smstwilio

Inicia el entorno virtual ejecutando:

    $ source smstwilio/bin/activate

### Instalar Django, Twilio
Antes de hacer eso, debemos asegurarnos que tenemos la última versión de pip, el software que utilizamos para instalar Django:

    (smstwilio) ~$ python3 -m pip install --upgrade pip

Lo primero, crea un fichero requirements.txt dentro del directorio (nombre del directorio)/
Dentro del fichero nombre del directorio/requirements.txt deberías tener el siguiente texto:

    Django==2.2.5
    twilio==6.16.0

Ahora, ejecuta pip install -r requirements.txt para instalar Django, twilio.

    (smstwilio) ~$ pip install -r requirements.txt

### Inicio

Después de instalar nuestras dependencias, ahora creemos el proyecto Django:

    django-admin startproject SMSProject

Cree una aplicación para nuestra función sms:

    python manage.py startapp sms

Abra nuestra vista en sms / views.py y agregue el siguiente código:
    
    from django.http import HttpResponse
    from django.views.decorators.csrf import csrf_exempt
    
    from twilio.twiml.messaging_response import MessagingResponse
    
    @csrf_exempt
    def sms_response(request):
        # Start our TwiML response
        resp = MessagingResponse()
        # Add a text message
        msg = resp.message(“Hello, Tekerone!”)
        return HttpResponse(str(resp))
        
Ahora agregue una ruta a esta vista creando el archivo sms/urls.py y agregando el siguiente código:

    from django.conf.urls import url 
    from. importar vistas 
    urlpatterns = [ 
        url (r '^ $', views.sms_response, name = 'sms'), 
    ]
    
Lo siguiente es agregar nuestra ruta para la aplicación sms en la urls.py de nuestro proyecto, SMSProject. Navegue a SMSProject/urls.py y agregue este código:    

    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        url(r’^sms/’, include(‘sms.urls’)),
        url(r’^admin/’, admin.site.urls),
        ]

Ejecutemos nuestra aplicación ejecutando el comando en nuestra terminal:

    python manage.py runserver
    
Twilio necesita ver nuestra aplicación en Internet para que pueda administrar nuestra aplicación, recibir y enviar SMS. Podemos lograr esto ejecutando ngrok. Instala ngrok si no lo tienes. Puede ver cómo instalarlo visitando su sitio [aquí](https://ngrok.com/download).   

No olvides agregar ngrok a ALLOWED_HOSTS en nuestra configuración. En nuestra settings.py, asegúrese de agregar '.ngrok.io' o simplemente '*' (asterisco) para permitir todo.

Ejecutamos ngrok en la terminal:

    ngrok http 8000
    
copie el enlace ngrok, el https y agregue /sms/  en la url, ya que hace un tiempo creamos una ruta en nuestro urls.py , por lo que agregamos '/sms/' para el webhook tendrá acceso a nuestra vista.
Debería verse como esta URL de muestra:

    https: //{random-ngrok-url}/sms/
    
Busque los números de teléfono en su tablero de Twilio, haga clic en el número y lo dirigirá a la configuración de ese número. 
En la pestaña de configuración, desplácese hacia abajo y busque la sección de mensajes y reemplace el webhook predeterminado, 
  https://demo.twilio.com/welcome/sms/reply/.
Pegue la URL en esta sección de la configuración del número de teléfono.  
  
¡Intentemos enviar un mensaje al número que elegimos, y voila~!  
