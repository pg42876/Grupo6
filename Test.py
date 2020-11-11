import unittest
import AASB

class TestAASB(unittest.TestCase):
    
    def test_tranforma(self):
        self.assertEqual(AASB.tranforma('Ficha 4.txt'), 'AAAAAAAGGGGGGGGGGG')
        self.assertEqual(AASB.tranforma('.txt'), 'O ficheiro não pode ser convertido numa seq')
        
    def test_FASTARead(self):
        self.assertEqual(AASB.FASTARead ('sequence.fasta'), 'CTCCGGATATCGACCCATAACGGGCAATGATAAAAGGAGTAACCTGTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAAATGACAAATGCCGGGTAACAATCCGGCATTCAGCGCCTGATGC')
        self.assertEqual(AASB.FASTARead ('.txt'), 'Não é um ficheiro Fasta' )
        self.assertEqual(AASB.FASTARead ('Py.txt'), 'O ficheiro não pode ser convertido numa seq')
        
    def test_complemento_inverso(self):
        self.assertEqual(AASB.complemento_inverso("ATGCGGTAGAGTCGAA"), "TTCGACTCTACCGCAT")
        self.assertEqual(AASB.complemento_inverso('267239807sgrtgsys'), "A string inserida não é considerado uma sequência")
        self.assertEqual(AASB.complemento_inverso('atgcggtagagtcgaa'), 'TTCGACTCTACCGCAT')
    
    
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
