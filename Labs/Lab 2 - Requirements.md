**Requerimientos**

- **Problema 1**

1. Es un requerimiento funcional, pues su enfoqué es relacionado con autenticación y niveles de autorización.
2. El requerimiento mezcla requerimientos funcionales, así como requerimientos no funcionales

Para que el requerimiento sea 100% funcional tendría que omitirse la parte específica del sistema y software que se va a utilizar.

1. El requerimiento no cuenta con la estructura y el detalle para ser un requerimiento funcional, al ser este un requerimiento de autenticación debe estar estructurado de la siguiente manera:

_&quot;2.5. Restricciones Generales_

_Acerca del arquitecto:_

- _El arquitecto designará al personal autorizado como auxiliar en el manejo del sistema._
- _Para ello, otorgará una contraseña única de 8 caracteres, para que el designado pueda ejecutar ingresar y ejecutar cualquier función del sistema._
- _El software que utilizará el arquitecto deberá ser ejecutado en su computadora._

_Acerca del personal autorizado_

- _El personal autorizado deberá confirmar cualquier función del sistema ingresando una contraseña de 8 caracteres._

_Acerca de la contraseña_

- _La contraseña proporcionada deberá tener entre 4 y 8 caracteres de longitud_
  - _La contraseña debe contener sólo letras y números._
  - _La contraseña debe contener al menos un número y una letra._
  - _La contraseña es sensible a mayúsculas._
- _Mostrar mensajes de error si se ha dejado en blanco el cuadro de texto de password._
- _El sistema bloqueará la operación después de ingresar una contraseña equivocada más de 3 veces._
- _El sistema volverá a funcionar luego de 5 minutos.&quot;_

- **Problema 2**

1. Es un requerimiento no funcional.
2. Está estructurado de una manera demasiado redundante y sin ser objetiva y concisa. La redacción correcta sería de la siguiente manera:

**&quot;Seguridad**

_Es un error asumir que el programa no tendría problemas de seguridad y a su vez, omitir._

_este requisito. los errores de seguridad pueden surgir de medios tanto internos como externos._

_En ese caso, los profesores deberán ingresar una contraseña para acceder al esquema._

**Disponibilidad**

_La aplicación será disponible en formato de CD._

_La aplicación será accesible por el público en general._

**Mantenimiento**

_El equipo de desarrollo será capaz de agregar una nueva característica al programa, incluyendo código_

_fuente, modificaciones documentadas y testing en un tiempo de una semana de trabajo._

**Confiabilidad**

_La aplicación será completamente funcional en cualquier plataforma que tenga_

_un buscador web que tenga Javascript habilitado, funciones de audio y plug-in de Flash.&quot;_

- **Problema 3**

1. Es un requerimiento no funcional.
2. Debido a que es un tema de escalabilidad, el requerimiento hace énfasis en detalles funcionales que pueden omitirse.
3. La redacción puede ser más reducida, siendo de la siguiente manera:

_&quot;The project should be scalable to accommodate unrestricted growth in the number of payboxes to be plugged into the Turnstile system&quot;_

- **Problema 4**

1. Es un requerimiento funcional.
2. El requerimiento esta mostrado como una síntesis de lo que debe hacer el sistema y no estructurado con las características de un requerimiento funcional.
3. Es muy genérico y no divide las diferentes características de lo que debe hacer el sistema, la redacción adecuada sería:

_&quot;ID: FR1_

_TITLE: Access the application web page._

_DESC:_

- _The user should be able to access the application web page through any web browser._

_RATIONAL: In order for a user to access the webpage_

_DEP: NONE_

_ID: FR2_

_TITLE: Web application - Search_

_DESC:_

- _Given that a user accessed the webpage, then the first page that is shown should be the search page._
- _The user should be able to search for a crossing, according to several search options._
- _The user should write the first letter of the crossing street name and a part of the crossing street name._

_RATIONAL: In order for a user to search for a street name_

_DEP: FR1_

_ID: FR3_

_TITLE: Web application - Search result in a map view_

_DESC:_

-
  - _Search results can be viewed on a map according to the user&#39;s inputs._
  - _A specific pin will represent the specific crossing location._
  - _The map view should include a button that, when selected should display satellite view._

_RATIONAL: The way results are displayed in a map_

_DEP: FR2&quot;_

- **Problema 5**

1. Es un requerimiento funcional pues hace énfasis en ciertas funciones administrativas.
2. El requerimiento es muy repetitivo y podría consolidarse.
3. El requerimiento esta mostrado como una síntesis y con redundancia en las operaciones DML de lo que debe hacer el sistema, no está estructurado con las características de un requerimiento funcional al igual que en el caso anterior, la redacción adecuada sería:

Mensajes de confirmación

_&quot;ID: FR1_

_TITLE: Alta, baja y edición_

_DESC:_

- _El usuario será capaz de realizar operaciones DML a la base de datos del sistema para ejecutar las siguientes operaciones:_
  - _Dar de alta un elemento de la base de datos._
  - _Dar de baja un elemento de la base de datos._
  - _Editar un elemento de la base de datos._

_RATIONAL: Cualquier nuevo hallazgo debe ser documentado en la base de datos._

_DEP: Deben existir las tablas o los esquemas para poder realizar las operaciones._

_ID: FR2_

_TITLE: Mensajes de confirmación_

_DESC:_

- _El sistema será capaz de mandar un mensaje de confirmación antes de concretar operaciones que la soliciten._

_RATIONAL: Operaciones que cambien el estado de la base de datos._

_DEP: FR1&quot;_