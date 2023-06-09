from imports import str_to_calculations as stc
import unittest
from imports import funciones as fn

class TestStrToCalc(unittest.TestCase):

    def test_blanca_tokenizer_1(self):
        res = stc.tokenize("a+b")
        self.assertEqual(res, ['a','+','b'])

    def test_blanca_tokenizer_2(self):
        res = stc.tokenize("a-b")
        self.assertEqual(res, ['a','-','b'])

    def test_blanca_tokenizer_3(self):
        res = stc.tokenize("a*b")
        self.assertEqual(res, ['a','*','b'])

    def test_blanca_tokenizer_4(self):
        res = stc.tokenize("a/b")
        self.assertEqual(res, ['a','/','b'])

    def test_blanca_tokenizer_5(self):
        res = stc.tokenize("a|b")
        self.assertEqual(res, ['a','|','b'])

    def test_blanca_tokenizer_6(self):
        res = stc.tokenize("a=b")
        self.assertEqual(res, ['a','=','b'])

    def test_blanca_tokenizer_7(self):
        res = stc.tokenize("a")
        self.assertEqual(res, ['a'])

    def test_blanca_tokenizer_8(self):
        res = stc.tokenize("abcd")
        self.assertEqual(res, ["abcd"])

    def test_blanca_parser_11(self):
        res = stc.parser(['1'])
        self.assertEqual(res, [1])

    def test_blanca_parser_3(self):
        res = stc.parser([''])
        self.assertEqual(res, [])

    def test_blanca_parser_1_2_11_16(self):
        res = stc.parser(['1','|','2'], fn.hacer_fraccion)
        self.assertEqual(res, [(1,2)])

    def test_blanca_parser_1_2_11_15(self):
        res = stc.parser(['1','|','2', '3'], fn.hacer_fraccion)
        self.assertEqual(res, [(1,2),3])

    def test_blanca_parser_11_12(self):
        crash =False
        try:
            stc.parser(['1','|','2'])
        except:
            crash = True
        self.assertTrue(crash)

    def test_blanca_parser_13(self):
        res = stc.parser(['|'], fn.hacer_fraccion)
        self.assertEqual(res, ['|'])

    def test_blanca_parser_14_3(self):
        res = stc.parser(['|', ''], fn.hacer_fraccion)
        self.assertEqual(res, ['|'])

    def test_blanca_parser_8(self):
        crash =False
        try:
            stc.parser(['+'])
        except:
            crash = True
        self.assertTrue(crash)

    def test_blanca_parser_4_11(self):
        res = stc.parser(['1','+'])
        self.assertEqual(res, [1,'+'])

    def test_blanca_parser_5(self):
        res = stc.parser(['1','-'])
        self.assertEqual(res, [1,'-'])

    def test_blanca_parser_6(self):
        res = stc.parser(['1','*'])
        self.assertEqual(res, [1,'*'])

    def test_blanca_parser_7(self):
        res = stc.parser(['1','/'])
        self.assertEqual(res, [1,'/'])

    def test_blanca_parser_9(self):
        crash =False
        try:
            stc.parser(['='])
        except:
            crash = True
        self.assertTrue(crash)

    def test_blanca_parser_10(self):
        res = stc.parser(['1','='])
        self.assertEqual(res, [1,'=',' '])

if __name__ == "__main__":
    unittest.main()
