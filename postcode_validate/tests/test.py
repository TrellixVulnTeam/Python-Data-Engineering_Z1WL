
import unittest

from postcodevalidate import func


class TestMainModule(unittest.TestCase):

    def test_postcode_validator(self):
        
        ## list of valid and in-valid postcodes for testing!
        pos_validators=['EC1A 1BB','EC1A1BB','W1A 0AX','ec1A 1BB']  
        neg_validators=['EC1A 11B','EC1A1BB1','123']
        
        for char in pos_validators:
            self.assertTrue(func.postcode_validator(char))
        for neg_char in neg_validators:
            self.assertFalse(func.postcode_validator(neg_char))

            
if __name__ == "__main__":
    unittest.main()
