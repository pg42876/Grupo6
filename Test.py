import unittest
import AASB


class TestAASB(unittest.TestCase):
    
    #def setUp(self):
        #self.AASB = AASB.transforma('Ficha 4.txt')
    
    def test_transforma(self):
        self.assertEqual(AASB.transforma('Ficha 4.txt'), 'AAAAAAAGGGGGGGGGGG')
        self.assertRaises(Exception, 'O ficheiro não pode ser convertido numa seq', AASB.transforma )
            
        
    def test_FASTARead(self):
        self.assertEqual(AASB.FASTARead ('sequence.fasta'), 'CTCCGGATATCGACCCATAACGGGCAATGATAAAAGGAGTAACCTGTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAAATGACAAATGCCGGGTAACAATCCGGCATTCAGCGCCTGATGC')
        self.assertRaises(Exception, 'O ficheiro não pode ser convertido numa seq', AASB.FASTARead)
        
    def test_complemento_inverso(self):
        self.assertEqual(AASB.complemento_inverso("ATGCGGTAGAGTCGAA"), "TTCGACTCTACCGCAT")
    
    def test_transcricao(self):
        self.assertEqual(AASB.transcricao("ATGCGGTAGAGTCGAA"), 'AUGCGGUAGAGUCGAA')
        
    def test_traducao(self):
        self.assertEqual(AASB.traducao("ATGCGGTAGAGTCGAA"), "MR_SR")
        
    def test_validarseq(self):
        self.assertEqual(AASB.validarseq("ATGCGGTAGAGTCGAA"), True)
        self.assertEqual(AASB.validarseq("fdyfugfufgufjfyk"), False)
        self.assertEqual(AASB.validarseq(""), False)
    
    def test_contar_bases(self):
        self.assertEqual(AASB.contar_bases("ATGCGGTAGAGTCGAA"), {'A': 5, 'T': 3, 'G': 6, 'C': 2})
        
    def test_reading_frames(self):
        self.assertEqual(AASB.reading_frames("ATGCGGTAGAGTCGAA"),['MR_SR', 'CGRVE', 'AVES', 'FDSTA', 'STLPH', 'RLYR'])
        
    def test_proteins(self):
        self.assertEqual(AASB.proteins("CTCCGGATATCGACCCATAACGGGCAATGATAAAAGGAGTAACCTGTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAAATGACAAATGCCGGGTAACAATCCGGCATTCAGCGCCTGATGC"),['MQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDHGWWKQHYEWRGNRWHLHGPPPPPRHHKKAPHDHHGGHGPGKHHR_','MEVTGATTAGGNNIMNGEAIAGTYTDRRHRRATIRKLLMIITAVMVQANITAK_','MIKGVTCEKDAIYRTRTFPGSGRSHGSTGCGNYVSPVSKITDRRS_','MFAWTMTAVMIMRSFLMVARRWRRSV_','MLFPPAVVAPVTSIPVIATIITIAYL_','MARQSLAPTRTAATAAPP_','MSGYRPITGNDKRSNL_','MPDCYPAFVI_','MPGNNPAFSA_','MGRYPEIRR_','MTNAG_'] )
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
