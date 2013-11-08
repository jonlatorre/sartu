Aplicación de control Sartu
=====================


Esta es una pequeña aplicaciñon para controlar la red de la asociación Sartu Alava

Está basada en el proyecto https://github.com/pinax/pinax-project-account

Para ponerla en marcha
 * git clone https://github.com/jonlatorre/sartu.git
 * cd sartu
 * virtualenv .
 * . ./bin/activate
 * pip install -r requirements
 * Editar la conf
 * ./manage syncdb
 * ./manage runserver
