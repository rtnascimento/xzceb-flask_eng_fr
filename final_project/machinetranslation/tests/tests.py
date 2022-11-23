import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_null(self): 
        self.assertIsNone(english_to_french(None))
    def test_translation(self): 
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test_null(self): 
        self.assertIsNone(french_to_english(None))
    def test_translation(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        
        
unittest.main()