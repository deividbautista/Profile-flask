
//-------------------------------------------------------
//Sección donde definiremos todas las constantes que utiliaremos
//para brindar la funcionalidad ocultar y ver contraseña.
//-------------------------------------------------------

//Esto se realiza a travez del query selector, el cual nos permite 
//selecciónar un elemento de nuestro html y darle funciones.
const iconEye = document.querySelector('#icon-eye')
const password = document.querySelector('#password')
const eye = document.querySelector('#eye')
//-------------------------------------------------------
//Sección de funcionalidad para ver y ocultar contraseña.
//-------------------------------------------------------

//Utilizamos la contante definida anteriormente, le brindamos el 
//evento click, en pocas palabras, cuando se seleccione el objeto 
//realizara lo siguiente.
iconEye.addEventListener('click', () =>{

    //Definimos la condicional if, en la que si el tipo del input
    //es igual a password, tenemos el primer estado en el que al moomento
    //de dar click se realizara lo que determinemos dentro del if.
    if (password.type === 'password'){

        //Se cambia el tipo del input, por text.
        password.type = 'text'

        //Se remueve la clase, que nos da el icono del ojo cerrado.
        eye.classList.remove('fa-eye-slash')

        //Se añade la clase para el ojo abierto.
        eye.classList.add('fa-eye')

      //En cuyo caso que la condicional no se cumpla, osea que el imput sea
      //tipo text, se procedera a realizar lo determiinado en el if, en el
      //momento de seleccionar el elemento.
    } else{
        //Se cambia el tipo del input, por password.
        password.type = 'password'
        //Se remueve la clase para el ojo abierto.
        eye.classList.remove('fa-eye')
        //Se añade la clase para el el icono del ojo cerrado.
        eye.classList.add('fa-eye-slash')
    }

})