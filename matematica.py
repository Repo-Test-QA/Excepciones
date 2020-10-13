class matematica:

    def sumar(self, nro1, nro2):            # self, se usa para variables que son de la clase

        try:
            if nro1 < 0:
                raise Exception('Los números tienen que se positivos')  # levantar una excepción
        except:
            return 'Debe ingresar un número mayor a cero'
        else:
            return nro1 + nro2


        #if nro1 < 0:
        #    return 'Debe ingresar un número mayor a cero'
        #else:
        #    return nro1 + nro2


    def restar(self, nro1, nro2):
        return nro1 - nro2


    def multiplicar(self, nro1, nro2):

        # Yo puedo redefinir ciertas excepciones.
        # En este caso solo va a funcionar la operación con nros. enteros
        try:
            if not type(nro1) is int:
                raise TypeError('Only integers')
        except TypeError:
            return 'No puedo multiplicar'
        else:
            return nro1 * nro2

    def dividir(self, nro1, nro2):

        n1 = nro1 - 5
        n2 = nro2 - 3
        n3 = 0

        try:                        # Intenta hacerme un retorno entre nro1 y nro2
            n3 = n1 / n2            # return nro1 / nro2

        except ZeroDivisionError:   # Intente dividir pero no puede, estas excepciones son las que nos da el lenguaje Python => ZeroDivisionError
            return 'No puedo dividir por cero'

        except TypeError:           # Tipo de dato
            return 'Debe ingresar numeros'
        else:                       # Sino pasa por ninguna excepción retorna n3 es decir 0.0
            return n3

        finally:                    # Si quiero ejecutar un bloque de código y no me interesa que suceda con el Try y las excepciones
                                    # Utilizamos Finally.
            print('Hola quiero dividir')

        # Que pasa si quiero armar mis propias excepciones
        # Al sumar, el 1ero nro es menor a cero no debería ser sumado



class mapas:
    def get_item(self, mapa, item):
        try:
            return mapa[item]
        except KeyError:
            return 'No existe la Key'


mi_calculadora = matematica()

# Ahora el mensaje que se muestra es 'No puedo dividir por cero', ahora se entiende lo que esta pasando
print(mi_calculadora.dividir(5, 7))
print(mi_calculadora.sumar(2, 2))
print(mi_calculadora.sumar(-1, 8))
print(mi_calculadora.multiplicar(2, 4))
print(mi_calculadora.multiplicar('Hi', 8))

mi_mapa = mapas()      # -------- Dict mapa -------  -- Item --
print(mi_mapa.get_item({'id': 2, 'nombre': 'Pablo'}, 'id'))
print(mi_mapa.get_item({'id': 2, 'nombre': 'Pablo'}, 'nombre'))
# Ingresando una Key que no existe. se muestra un tipo de excepcion => KeyError
# Agregamos a la clase mapas un try y excepción que controles este escenario.
print(mi_mapa.get_item({'id': 2, 'nombre': 'Pablo'}, 'apellido'))


# Otro ejemplo un diccionario, que tiene dos elementos.
#mi_mapa = {'id': 1, 'nombre': 'Pablo'}
# Verifico los valores de las Keys id y nombre
#print(mi_mapa['id'])
#print(mi_mapa['nombre'])
# Cuando quiero verificar una Key que no existe en el diccionario,
# se muestra un tipo de excepcion => KeyError
#print(mi_mapa['apellido'])


# Con los conocimientos de las excepciones, vamos a regresar a nuestro proyecto de
# tienda de ropa, especificamente al archivo pageIndex, para aplicar estas
# excepciones.