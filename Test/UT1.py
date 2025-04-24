import unittest

class Test_String(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('kali'.upper(),'KALI')

    def test_isupper(self):
        self.assertTrue('KALI'.isupper())
        self.assertFalse('Kali'.islower())
    def sum_n(self):
        self.a = 10
        self.b = 5
        return self.a + self.b

    def test_sum(self):
        self.assertEqual(self.sum_n(),15)


    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(),['Hello','World'])

        with self.assertRaises(TypeError):
            s.split(2) #invalid argument

if __name__ == '__main__':
    unittest.main(verbosity=2)