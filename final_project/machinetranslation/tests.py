import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test_null(self): 
        self.assertIsNone(englishToFrench(None))
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test_null(self): 
        self.assertIsNone(englishToFrench(None))
        
        
unittest.main()