from imports import str_to_calculations as stc
import unittest

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

if __name__ == "__main__":
    unittest.main()
