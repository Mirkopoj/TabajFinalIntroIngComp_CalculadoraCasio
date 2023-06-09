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

    #def test_no_str(self):
        #crash = False
        #try:
            #stc.tokenize(1)
        #except:
            #crash = True
        #self.assertTrue(crash)

    def test_sin_caracteres_especiales(self):
        res = stc.tokenize("abc123@!?\"%#")
        self.assertEqual(res, ["abc123@!?\"%#"])

    def test_suma(self):
        res = stc.tokenize("abc123+!?\"%#")
        self.assertEqual(res, ["abc123","+","!?\"%#"])

    def test_resta(self):
        res = stc.tokenize("abc123-!?\"%#")
        self.assertEqual(res, ["abc123","-","!?\"%#"])

    def test_multiplicacion(self):
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

if __name__ == "__main__":
    unittest.main()
