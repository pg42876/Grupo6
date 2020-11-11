import unittest
import AASB

class TestAASB(unittest.TestCase):
    
    def test_tranforma(self):
        my_file = AASB.tranforma("C:/Users/luism/OneDrive/Documentos/GitHub/Grupo6/Ficha 4.txt")
        self.assertEqual(my_file, 'AAAAAAAGGGGGGGGGGG')
        
    def test_FASTARead(self):
        seq = AASB.FASTARead ("C:/Users/luism/Downloads/sequence.fasta")
        self.assertEqual(seq, 'CTCCGGATATCGACCCATAACGGGCAATGATAAAAGGAGTAACCTGTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAAATGACAAATGCCGGGTAACAATCCGGCATTCAGCGCCTGATGC')
        
    def test_complemento_inverso(self):
        seq = AASB.complemento_inverso("ATGCGGTAGAGTCGAA")
        self.assertEqual(seq, "TTCGACTCTACCGCAT")
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
