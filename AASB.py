def genecode():
    genecode = {
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
    return genecode

def transforma(filename):
    """
Recebe um ficheiro txt cotendo uma sequância de bases e devolve a sequência do ficheiro.

PARAMETERS
----------
txt: ficheiro txt a ser aberto
    É uma sequência de bases de um DNA.

returns: Uma string da sequência do ficheiro em letras maiúsculas.
Exception: O ficheiro não pode ser convertido numa sequência.
"""
    my_file = open(filename)
    my_file = my_file.readline()
    if validarseq(my_file) == True:
        my_file = my_file.upper()
        return(my_file)
    raise Exception('O ficheiro não pode ser convertido numa seq')

def FASTARead(filename):
    """
Recebe um ficheiro FASTA  e devolve o conteúdo do ficheiro.

PARAMETRES
----------
FASTA: ficheiro no formato FASTA.
    É uma sequência de bases de um DNA.

returns: Uma string apenas com as linhas das bases, concatenadas, em letras maiúsculas.
Exception: O ficheiro não pode ser convertido numa sequência
    """
    with open(filename, 'r') as readfile:
        seq = readfile.readlines()[1:]
        seq = [x.replace('\n', '') for x in seq]
        seq = ''.join(seq)
        
        if validarseq(seq) == True:
            seq = seq.upper()
            return(seq)
        raise Exception('O ficheiro não pode ser convertido numa seq')

def complemento_inverso(seq):
    """
Função que recebe uma sequência de DNA e devolve o complemento inverso dessa sequência.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.

returns: Uma string com o complemento inverso da sequência, caso a sequência seja válida.
"""
    seq = seq[::-1]
    seq = seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return(seq)
    
def transcricao(seq):
    """
Função que recebe uma sequência de DNA e devolve o transcrito dessa sequência.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.

returns: Uma string com o complemento inverso da sequência, caso a sequência seja válida.
"""
    return (seq.replace('T', 'U'))

def traducao(seq):
    """
Função que recebe uma sequência de DNA e devolve as possiveis sequências de aminoácidos.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.

returns: Devolve a Tradução de um sequência de DNA
    """
    gene = genecode()
    import re
    DNA = re.findall('...', seq)
    t = []
    for y in DNA:
        t.append(gene[y])
    result=''.join(t)
    return(result)
    
def validarseq(seq):
    """
Função que recebe uma sequência de bases que para ser validada como DNA.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.

returns: True se a sequência for válida e False se a sequência não for válida.    
    """
    seq = seq.upper()
    if seq == "":
        return (False)
    elif len(set(seq) - {'A','C','G','T'})==0:
        return (True)
    else:
        return (False)

def contar_bases(seq):
    """
Função que recebe uma sequência de DNA e conta o número de bases da sequência.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.
    
returns: Um dicionário em que uma chave corresponde a um caracter da sequência e o valor dessa chave corresponde ao número de ocorrências desse caracter na sequência, caso a sequência seja válida.
         A ordem das chaves no dicionário corresponde à ordem de aparecimento dos caracteres na sequência.
    """
    nucleotidos = {}
    for x in seq:
        if x not in nucleotidos:
            nucleotidos [x]= 0
        nucleotidos[x]+= 1
    return(nucleotidos)

def reading_frames(seq):
    """
Função que recebe uma sequência de DNA e devolve os codões presentes na sequência.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.
    
returns: Devolve todos os codões presentes no DNA começando a tradução na posição 1, 2 e 3, e a tradução do inverso nas posições 1, 2 e 3 da mesma sequência de DNA  
    """
    seq_inv = complemento_inverso(seq)
    l1 = []
    for x in range(3):
        l1.append(traducao(seq_inv[x:]))
    l2 = []
    for a in range(3):
        l2.append(traducao(seq[a:]))
    l3 = []
    l3 = l2 + l1
    return(l3)

def proteins(seq):
    """
Função que recebe uma sequência de DNA e devolve a sequência das proteínas possíveis.

PARAMETERS
----------
seq: string
    É uma sequência de DNA.
    
returns: Uma ou mais listas com a sequência aminoacidica das proteínas possíveis, traduzidas a partir dessa sequência, caso a sequência seja válida.
         Uma lista vazia corresponde a uma sequência de DNA inicial sem proteínas possíveis, caso a sequência seja válida.
    """
    import re
    traducao = reading_frames(seq)
    traducao = ''.join(traducao)
    proteina = []       
    proteina.extend(re.findall('M.*?_', traducao))

    def customkey(proteina):
        return -len(proteina), proteina
    proteina = list(dict.fromkeys(proteina))
    proteina = sorted(proteina, key = customkey)
    return(proteina)
    






        







    


    
