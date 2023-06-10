from imports import str_to_calculations as stc
import unittest
from imports import funciones as fn

class TokenizerBlanca(unittest.TestCase):

    def test_1(self):
        res = stc.tokenize("a+b")
        self.assertEqual(res, ['a','+','b'])

    def test_2(self):
        res = stc.tokenize("a-b")
        self.assertEqual(res, ['a','-','b'])

    def test_3(self):
        res = stc.tokenize("a*b")
        self.assertEqual(res, ['a','*','b'])

    def test_4(self):
        res = stc.tokenize("a/b")
        self.assertEqual(res, ['a','/','b'])

    def test_5(self):
        res = stc.tokenize("a|b")
        self.assertEqual(res, ['a','|','b'])

    def test_6(self):
        res = stc.tokenize("a=b")
        self.assertEqual(res, ['a','=','b'])

    def test_7(self):
        res = stc.tokenize("a")
        self.assertEqual(res, ['a'])

    def test_8(self):
        res = stc.tokenize("abcd")
        self.assertEqual(res, ["abcd"])

class ParserBlanca(unittest.TestCase):

    def test_11(self):
        res = stc.parser(['1'])
        self.assertEqual(res, [1])

    def test_3(self):
        res = stc.parser([''])
        self.assertEqual(res, [])

    def test_1_2_11_16(self):
        res = stc.parser(['1','|','2'], fn.hacer_fraccion)
        self.assertEqual(res, [(1,2)])

    def test_1_2_11_15(self):
        res = stc.parser(['1','|','2', '3'], fn.hacer_fraccion)
        self.assertEqual(res, [(1,2),3])

    def test_11_12(self):
        crash = False
        try:
            stc.parser(['1','|','2'])
        except:
            crash = True
        self.assertTrue(crash)

    def test_13(self):
        res = stc.parser(['|'], fn.hacer_fraccion)
        self.assertEqual(res, ['|'])

    def test_14_3(self):
        res = stc.parser(['|', ''], fn.hacer_fraccion)
        self.assertEqual(res, ['|'])

    def test_8(self):
        crash = False
        try:
            stc.parser(['+'])
        except:
            crash = True
        self.assertTrue(crash)

    def test_4_11(self):
        res = stc.parser(['1','+'])
        self.assertEqual(res, [1,'+'])

    def test_5(self):
        res = stc.parser(['1','-'])
        self.assertEqual(res, [1,'-'])

    def test_6(self):
        res = stc.parser(['1','*'])
        self.assertEqual(res, [1,'*'])

    def test_7(self):
        res = stc.parser(['1','/'])
        self.assertEqual(res, [1,'/'])

    def test_9(self):
        crash = False
        try:
            stc.parser(['='])
        except:
            crash = True
        self.assertTrue(crash)

    def test_10(self):
        res = stc.parser(['1','='])
        self.assertEqual(res, [1,'=',' '])

class CalcBlanca(unittest.TestCase):

    def test_1(self):
        res = stc.calc(['='],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, ' ')

    def test_2_7(self):
        res = stc.calc([4,'/',2],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, 2)

    def test_3_7(self):
        res = stc.calc([4,'*',2],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, 8)

    def test_4_7(self):
        res = stc.calc([4,'+',2],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, 6)

    def test_5_7(self):
        res = stc.calc([4,'-',2],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, 2)

    def test_6(self):
        res = stc.calc([4],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, 4)

    def test_7_8(self):
        res = stc.calc([4,6],
                       fn.suma_clasica,
                       fn.resta_clasica,
                       fn.multiplicacion_clasica,
                       fn.division_clasica)
        self.assertEqual(res, None)

class TokenizerNegra(unittest.TestCase):

    ##  tokenize(): ###
    #
    #   tokenize recibe un str y devuelve una list[str]
    #   
    #   Promete aislar los caracteres especiales: 
    #       +   -   *   /   |   =
    #   dando como resultado una lista del tipo: 
    #   ["izq", "especial", "mid", ... , "mid", "especial", "der"]
    #   Cuando no hay nada antes, despues o entre medio de los 
    #   caracteres especiales se espera un str vacio, "".
    #   Por ejemplo, para "2+2=" se espera obtener
    #   ["2", "+", "2", "=", ""]
    #
    ###################

    def test_sin_caracteres_especiales(self):
        res = stc.tokenize("abc123@!?\"%#")
        self.assertEqual(res, ["abc123@!?\"%#"])

    def test_suma(self):
        res = stc.tokenize("abc123+!?\"%#")
        self.assertEqual(res, ["abc123","+","!?\"%#"])

    def test_resta(self):
        res = stc.tokenize("abc123-!?\"%#")
        self.assertEqual(res, ["abc123","-","!?\"%#"])

    def test_multiplicación(self):
        res = stc.tokenize("abc123*!?\"%#")
        self.assertEqual(res, ["abc123","*","!?\"%#"])

    def test_divicion(self):
        res = stc.tokenize("abc123/!?\"%#")
        self.assertEqual(res, ["abc123","/","!?\"%#"])

    def test_igual(self):
        res = stc.tokenize("abc123=!?\"%#")
        self.assertEqual(res, ["abc123","=","!?\"%#"])

    def test_fraccion(self):
        res = stc.tokenize("abc123|!?\"%#")
        self.assertEqual(res, ["abc123","|","!?\"%#"])

    def test_combinado(self):
        res = stc.tokenize("a/bc*23+!?-%#|\\)=$&")
        self.assertEqual(res, ["a","/","bc","*","23","+","!?","-","%#","|","\\)","=","$&"])

    def test_solo_especiales(self):
        res = stc.tokenize("+-*/|=")
        self.assertEqual(res, ["","+","","-","","*","","/","","|","","=",""])

class ParserNegra(unittest.TestCase):

    ##  parser(): #####
    #
    #   parser recibe una list[str] 
    #   y devuelve una lista con tipos de dato mixtos
    #   
    #   Promete ignorar los caracteres especiales: 
    #       +   -   *   /   =
    #   mientras convierte a enteros todos los otros str
    #   
    #   si se le da una función para generar fracciones 
    #   tratará el caracter | como un caracter especial,
    #   llamando la función dada con el valor previo y el 
    #   valor siguiente, solo si el valor siguiente existe.
    #
    #   ej. parser(["1","|","2"], funcion_auxiliar)
    #   convertirá los str "1" y "2" a numeros enteros
    #   y llamará a: ret = funcion_auxiliar(1,2) 
    #   ret será lo que guarde en la lista.
    #   
    #   Si no se provee esta funcion, el caracter | resulta 
    #   en un error.
    #
    #   dando como resultado una lista del tipo: 
    #   [num, "especial", num, ... , num, "especial", num]
    #   o
    #   [frac, "especial", frac, ... , frac, "especial", frac]
    #   si se le da una fucion para generar fracciones.
    #
    #   Cada vez que encuentre un caracter especial, corroborará
    #   que el elemento previo en la lista sea del tipo adecuado
    #   los tipos que se esperan obtener son int cuando no se 
    #   provee una función para generar fracciones y tuple[int,int]
    #   cuando si se provee. Esto marca una pauta para como se deben
    #   representar las fracciones y el tipo de dato que la fucion 
    #   generadora de fracciones debe devolver.
    #
    ###################

    def test_numero_solo(self):
        res = stc.parser(["42"])
        self.assertEqual(res, [42])

    def test_caracter_especial_solo(self):
        crash = False
        try:
            stc.parser(["+"])
        except:
            crash = True
        self.assertTrue(crash)

    def test_combinado(self):
        res = stc.parser(["42","+","24"])
        self.assertEqual(res, [42,"+",24])

    def test_fraccion_sola(self):
        res = stc.parser(["42","|","21"], fn.hacer_fraccion)
        self.assertEqual(res, [(42,21)])

    def test_combinado_fracciones(self):
        res = stc.parser(["42","|","21","+","52","|","31"], fn.hacer_fraccion)
        self.assertEqual(res, [(42,21),"+",(52,31)])

    def test_fraccion_sola_sin_funcion(self):
        crash = False
        try:
            stc.parser(["42","|","21"])
        except:
            crash = True
        self.assertTrue(crash)

    def test_hacer_frac_sin_datos(self):
        res = stc.parser(["|"], fn.hacer_fraccion)
        self.assertEqual(res, ["|"])

    def test_hacer_frac_sin_dato_previo(self):
        crash = False
        try:
            stc.parser(["|", "3"], fn.hacer_fraccion)
        except:
            crash = True
        self.assertTrue(crash)

    def test_caracter_no_especial(self):
        crash = False
        try:
            stc.parser(["a"])
        except:
            crash = True
        self.assertTrue(crash)

class CalcNegra(unittest.TestCase):

    ##  calc(): #######
    #
    #   calc recibe una lista de tipo mixto y funciones para sumar,
    #   restar, multiplicar y dividir. No tiene un tipo definido 
    #   para devolver. Se le puede pasar una función opcional para 
    #   simplificar las fracciones.
    #   
    #   Trata los siguientes caracteres como especiales:
    #       +   -   *   /   =
    #
    #   calc recorre la lista que recibe y cuando encuentra un 
    #   caracter especial, opera.
    #   
    #   Si encuentra un = imprime toda la expresión a la izquierda 
    #   del = inclusive, y luego imprime el resultado de pasar la
    #   toda la lista a la izquierda del igual a calc.
    #
    #   Cuando encuentra un +, -, * o / llama a la función de suma 
    #   resta, multiplicación o división, respectivamente. A estas 
    #   funciones se les pasa como parámetro los resultados de llamar 
    #   a calc con la expresión a la izquierda del operador y la 
    #   expresión a la derecha.
    #
    #   ej.:
    #       clac([1,"*",2,"+",3,"*",4], sum, res, mult, div)
    #       al encontrar "+", llamará a 
    #       sum(
    #           calc([1,"*",2], sum, res, mul, div), 
    #           calc([3,"*",4], sum, res, mul, div), 
    #       )
    #
    #   En caso de que calc reciba una lista de largo 1, devuelve su único 
    #   elemento.
    #
    #   Los caracteres especiales se buscan en pasadas independientes, de
    #   no ser así las operaciones se resolverian de izquierda a derecha, 
    #   sin precedencia de operadores. Los caracteres se buscan en el 
    #   siguiente orden, =, +, -, /, *. De este modo la expresión se 
    #   evalúa en el orden inverso a como se buscan los operadores.
    #
    #   ej.: 
    #       (No se escriben las funciones de suma, resta, 
    #        multiplicación y división, para simplificar)
    #       si se llama a calc con la siguiente lista:
    #       [1,"*",2,"+",3,"/",4,"-",5,"="]
    #       se resolverá:
    #
    #       print("1*2+3/4-5=", calc([1,"*",2,"+",3,"/",4,"-",5])
    #
    #       print("1*2+3/4-5=", 
    #           sum(
    #               calc([1,"*",2),
    #               calc([3,"/",4,"-",5])
    #           )
    #       )
    #
    #       print("1*2+3/4-5=", 
    #           sum(
    #               mul(1,2),
    #               res(
    #                   calc([3,"/",4),
    #                   calc[5]
    #               )
    #           )
    #       )
    #
    #       print("1*2+3/4-5=", 
    #           sum(
    #               2,
    #               res(
    #                   div(3,4),
    #                   5
    #               )
    #           )
    #       )
    #
    #       print("1*2+3/4-5=", 
    #           sum(
    #               2,
    #               res(
    #                   0.75,
    #                   5
    #               )
    #           )
    #       )
    #
    #       print("1*2+3/4-5=", 
    #           sum(
    #               2,
    #               -4.25
    #           )
    #       )
    #
    #       print("1*2+3/4-5=", -2.25)
    #
    ###################

    def a(self):
        return 1



if __name__ == "__main__":
    unittest.main()
