# test_CelsiusToFahrenheit.py
# Tests Temp Converter functions

import unittest
import CelsiusToFahrenheit
import re

class KnownValues(unittest.TestCase):
    # Set up
    def setUp(self):
        # get text from script for regex tests
        self.textfile = open('CelsiusToFahrenheit.py', 'r')
        self.scripttext = self.textfile.read()
    # Tear down
    def tearDown(self):
        # close the file
        self.textfile.close()
        
    ################################################
    # Test celsiusToFahrenheit()
    ################################################
    # For exception Handling
    def test_celsiusToFahrenheit_forTypeError(self):
        # Capture the results of the function
        result = CelsiusToFahrenheit.celsiusToFahrenheit("str")
        # Check for expected output
        self.assertEqual(-9999, result)
    def test_celsiusToFahrenheit_for10F_as_string(self):
        # Capture the results of the function
        result = CelsiusToFahrenheit.celsiusToFahrenheit("10")
        # Check for expected output
        self.assertEqual(-12.222222222222221, result)

    # For expected output
    def test_celsiusToFahrenheit_for0F(self):
        # Capture the results of the function
        result = CelsiusToFahrenheit.celsiusToFahrenheit(0)
        # Check for expected output
        self.assertEqual(32.0, result)

    def test_celsiusToFahrenheit_for100F(self):
        # Capture the results of the function
        result = CelsiusToFahrenheit.celsiusToFahrenheit(100)
        # Check for expected output
        self.assertEqual(212.0, result)

    def test_celsiusToFahrenheit_for55F(self):
        # Capture the results of the function
        result = CelsiusToFahrenheit.celsiusToFahrenheit(55)
        # Check for expected output
        self.assertEqual(131.0, result)
        

    def test_celsiusToFahrenheit_forMinus50F(self):
        # Capture the results of the function
        result = CelsiusToFahrenheit.celsiusToFahrenheit(-50)
        # Check for expected output
        self.assertEqual(-58.0, result)

    # Test regex search for a pattern in script
    def test_try_cmd_present(self):
        matches = re.findall("try:", self.scripttext)
        match = matches[0]
        self.assertEquals("try:", match)
        
    def test_except_block_present(self):
        matches = re.findall("except ValueError:", self.scripttext)
        matches += re.findall("except:", self.scripttext)
        hasMatch = bool(matches)
        self.assertEquals(True, hasMatch)
    

# Run the tests
if __name__ == '__main__':
    unittest.main()
    
