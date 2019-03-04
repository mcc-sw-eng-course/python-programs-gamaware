**Requerimientos**

- **Problema 1**

1. Es un requerimiento funcional, pues su enfoqu� es relacionado con autenticaci�n y niveles de autorizaci�n.
2. El requerimiento mezcla requerimientos funcionales, as� como requerimientos no funcionales

Para que el requerimiento sea 100% funcional tendr�a que omitirse la parte espec�fica del sistema y software que se va a utilizar.

1. El requerimiento no cuenta con la estructura y el detalle para ser un requerimiento funcional, al ser este un requerimiento de autenticaci�n debe estar estructurado de la siguiente manera:

_&quot;2.5. Restricciones Generales_

_Acerca del arquitecto:_

- _El arquitecto designar� al personal autorizado como auxiliar en el manejo del sistema._
- _Para ello, otorgar� una contrase�a �nica de 8 caracteres, para que el designado pueda ejecutar ingresar y ejecutar cualquier funci�n del sistema._
- _El software que utilizar� el arquitecto deber� ser ejecutado en su computadora._

_Acerca del personal autorizado_

- _El personal autorizado deber� confirmar cualquier funci�n del sistema ingresando una contrase�a de 8 caracteres._

_Acerca de la contrase�a_

- _La contrase�a proporcionada deber� tener entre 4 y 8 caracteres de longitud_
  - _La contrase�a debe contener s�lo letras y n�meros._
  - _La contrase�a debe contener al menos un n�mero y una letra._
  - _La contrase�a es sensible a may�sculas._
- _Mostrar mensajes de error si se ha dejado en blanco el cuadro de texto de password._
- _El sistema bloquear� la operaci�n despu�s de ingresar una contrase�a equivocada m�s de 3 veces._
- _El sistema volver� a funcionar luego de 5 minutos.&quot;_

- **Problema 2**

1. Es un requerimiento no funcional.
2. Est� estructurado de una manera demasiado redundante y sin ser objetiva y concisa. La redacci�n correcta ser�a de la siguiente manera:

**&quot;Seguridad**

_Es un error asumir que el programa no tendr�a problemas de seguridad y a su vez, omitir._

_este requisito. los errores de seguridad pueden surgir de medios tanto internos como externos._

_En ese caso, los profesores deber�n ingresar una contrase�a para acceder al esquema._

**Disponibilidad**

_La aplicaci�n ser� disponible en formato de CD._

_La aplicaci�n ser� accesible por el p�blico en general._

**Mantenimiento**

_El equipo de desarrollo ser� capaz de agregar una nueva caracter�stica al programa, incluyendo c�digo_

_fuente, modificaciones documentadas y testing en un tiempo de una semana de trabajo._

**Confiabilidad**

_La aplicaci�n ser� completamente funcional en cualquier plataforma que tenga_

_un buscador web que tenga Javascript habilitado, funciones de audio y plug-in de Flash.&quot;_

- **Problema 3**

1. Es un requerimiento no funcional.
2. Debido a que es un tema de escalabilidad, el requerimiento hace �nfasis en detalles funcionales que pueden omitirse.
3. La redacci�n puede ser m�s reducida, siendo de la siguiente manera:

_&quot;The project should be scalable to accommodate unrestricted growth in the number of payboxes to be plugged into the Turnstile system&quot;_

- **Problema 4**

1. Es un requerimiento funcional.
2. El requerimiento esta mostrado como una s�ntesis de lo que debe hacer el sistema y no estructurado con las caracter�sticas de un requerimiento funcional.
3. Es muy gen�rico y no divide las diferentes caracter�sticas de lo que debe hacer el sistema, la redacci�n adecuada ser�a:

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

1. Es un requerimiento funcional pues hace �nfasis en ciertas funciones administrativas.
2. El requerimiento es muy repetitivo y podr�a consolidarse.
3. El requerimiento esta mostrado como una s�ntesis y con redundancia en las operaciones DML de lo que debe hacer el sistema, no est� estructurado con las caracter�sticas de un requerimiento funcional al igual que en el caso anterior, la redacci�n adecuada ser�a:

Mensajes de confirmaci�n

_&quot;ID: FR1_

_TITLE: Alta, baja y edici�n_

_DESC:_

- _El usuario ser� capaz de realizar operaciones DML a la base de datos del sistema para ejecutar las siguientes operaciones:_
  - _Dar de alta un elemento de la base de datos._
  - _Dar de baja un elemento de la base de datos._
  - _Editar un elemento de la base de datos._

_RATIONAL: Cualquier nuevo hallazgo debe ser documentado en la base de datos._

_DEP: Deben existir las tablas o los esquemas para poder realizar las operaciones._

_ID: FR2_

_TITLE: Mensajes de confirmaci�n_

_DESC:_

- _El sistema ser� capaz de mandar un mensaje de confirmaci�n antes de concretar operaciones que la soliciten._

_RATIONAL: Operaciones que cambien el estado de la base de datos._

_DEP: FR1&quot;_