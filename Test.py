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
    
    def test_transcricao(self):
        self.assertEqual(AASB.transcricao("ATGCGGTAGAGTCGAA"), "UACGCCAUCUCAGCUU")
        self.assertEqual(AASB.transcricao("atgcggtagagtcgaa"), "UACGCCAUCUCAGCUU")
        self.assertEqual(AASB.transcricao("iywihio38927"), 'Não é um sequência válida de DNA')
        
    def test_traducao(self):
        self.assertEqual(AASB.traducao("ATGCGGTAGAGTCGAA"), "MR_SR")
        self.assertEqual(AASB.traducao("atgcggtagagtcgaa"), "MR_SR")
        self.assertEqual(AASB.traducao("hiohiohwiofhwoi3"), 'Cadeia de DNA inexistente')
        
    def test_validarseq(self):
        self.assertEqual(AASB.validarseq("ATGCGGTAGAGTCGAA"), True)
        self.assertEqual(AASB.validarseq("fdyfugfufgufjfyk"), False)
        self.assertEqual(AASB.validarseq(""), False)
    
    def test_contar_bases(self):
        self.assertEqual(AASB.contar_bases("ATGCGGTAGAGTCGAA"), {'A': 5, 'T': 3, 'G': 6, 'C': 2})
        self.assertEqual(AASB.contar_bases("atgcggtagagtcgaa"), {'A': 5, 'T': 3, 'G': 6, 'C': 2})
        self.assertEqual(AASB.contar_bases("khfklshflhfhoihw"), 'string apresentada não é uma sequência')
        
    def test_reading_frames(self):
        self.assertEqual(AASB.reading_frames("ATGCGGTAGAGTCGAA"),['MR_SR', 'CGRVE', 'AVES', 'FDSTA', 'STLPH', 'RLYR'])
        self.assertEqual(AASB.reading_frames("atgcggtagagtcgaa"),['MR_SR', 'CGRVE', 'AVES', 'FDSTA', 'STLPH', 'RLYR'])
        self.assertEqual(AASB.reading_frames("ffiuwhiofhiwfhiw"),'sequência inválida')
        
    def test_proteins(self):
        self.assertEqual(AASB.proteins("CTCCGGATATCGACCCATAACGGGCAATGATAAAAGGAGTAACCTGTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCAGCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGATAATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACATTATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCATAAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAAATGACAAATGCCGGGTAACAATCCGGCATTCAGCGCCTGATGC"),['MQSIVLALSLVLVAPMAAQAAEITLVPSVKLQIGDRDNRGYYWDGGHWRDHGWWKQHYEWRGNRWHLHGPPPPPRHHKKAPHDHHGGHGPGKHHR_', 'MEVTGATTAGGNNIMNGEAIAGTYTDRRHRRATIRKLLMIITAVMVQANITAK_', 'MIKGVTCEKDAIYRTRTFPGSGRSHGSTGCGNYVSPVSKITDRRS_', 'MFAWTMTAVMIMRSFLMVARRWRRSV_', 'MLFPPAVVAPVTSIPVIATIITIAYL_', 'MARQSLAPTRTAATAAPP_', 'MPDCYPAFVI_', 'MPGNNPAFSA_', 'MTNAG_'] )
        self.assertEqual(AASB.proteins("jfhkjsfhksgf89r"), 'seq inexistente')
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
