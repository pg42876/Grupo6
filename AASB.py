def tranforma():
    '''
    Função resposável por receber um ficheiro
    e de dar return de uma sequência em string
    '''
    filename = input ("filename: ")
    my_file = open(filename)
    my_file = my_file.readline()
    return(my_file)

def complemento_inverso():
    '''
    Função responsável por devolver o 
    complemento inverso de uma sequência de DNA
    '''
    seq = input('Introduza a sequência de DNA: ')
    seq = seq[::-1].upper()
    seq = seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
    return(seq)

def transcricao():
    '''
    Função responsável pela transcrição de DNA
    '''
    seq = input ('Introduza a sequência de DNA: ')
    seq_trans = seq.replace('A', 'u').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return (seq_trans)

def traducao():
    '''
    Função responsável pela tradução da cadeia de DNA
    '''
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

    cadeiaDNA= input()
    cadeiaDNA= cadeiaDNA.upper()
    def tradux(DNA): 
        import re
        DNA = re.findall('...', DNA)
        t = []
        for y in DNA:
            t.append(gencode[y])
        result=''.join(t)
        return(result)

    for a in range(3):
        return (tradux(cadeiaDNA[a:]))

traducao()







    


    
