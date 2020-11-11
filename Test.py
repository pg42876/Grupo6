import unittest
import AASB

class TestAASB(unittest.TestCase):
    
    def test_tranforma(self):
        self.assertEqual(AASB.tranforma('Ficha 4.txt'), 'AAAAAAAGGGGGGGGGGG')
        
    def test_FASTARead(self):
        self.assertEqual(AASB.FASTARead ('sequence.fasta'), 'CTCCGGATATCGACCCATAACGGGCAATGATAAAAGGAGTAACCTGTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAAATGACAAATGCCGGGTAACAATCCGGCATTCAGCGCCTGATGC')
        
    def test_complemento_inverso(self):
        self.assertEqual(AASB.complemento_inverso("ATGCGGTAGAGTCGAA"), "TTCGACTCTACCGCAT")
        self.assertRaises(expected_exception, callable, args, kwargs)
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
