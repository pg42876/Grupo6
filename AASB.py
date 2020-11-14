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

def tranforma(filename):
    '''
    Função responsável por receber um ficheiro
    e de dar return de uma sequência em string
    '''
    my_file = open(filename)
    my_file = my_file.readline()
    if validarseq(my_file) == True:
        my_file = my_file.upper()
        return(my_file)
    raise Exception('O ficheiro não pode ser convertido numa seq')

def FASTARead(filename):
    '''
    Função responsável por receber um ficheiro FASTA e
    devolve uma sequência
    '''
    with open(filename, 'r') as readfile:
        seq = readfile.readlines()[1:]
        seq = [x.replace('\n', '') for x in seq]
        seq = ''.join(seq)
        
        if validarseq(seq) == True:
            seq = seq.upper()
            return(seq)
        raise Exception('O ficheiro não pode ser convertido numa seq')

def complemento_inverso(seq):
    '''
    Função responsável por devolver o 
    complemento inverso de uma sequência de DNA
    '''
    seq = seq[::-1]
    seq = seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return(seq)
    
def transcricao(seq):
    '''
    Função responsável pela transcrição de DNA
    '''
    return (seq.replace('T', 'U'))

def traducao(seq):
    '''
    Função responsável pela tradução da cadeia de DNA
    '''
    gene = genecode()
    import re
    DNA = re.findall('...', seq)
    t = []
    for y in DNA:
        t.append(gene[y])
    result=''.join(t)
    return(result)
    
def validarseq(seq):
    '''
    Função responsável por verificar 
    se uma sequência é válida ou não
    '''
    seq = seq.upper()
    if seq == "":
        return (False)
    elif len(set(seq) - {'A','C','G','T'})==0:
        return (True)
    else:
        return (False)

def contar_bases(seq):
    '''
    Função que conta as bases de uma sequência e
    devolve um dicionário com a contagem
    '''
    nucleotidos = {}
    for x in seq:
        if x not in nucleotidos:
            nucleotidos [x]= 0
        nucleotidos[x]+= 1
    return(nucleotidos)

def reading_frames(seq):
    '''
    Função que devolve uma lista com as reading frames
    '''
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
    '''
    Função que devolve a lista de todas
    as proteínas ordenadas por tamanho e 
    por ordem alfabética para as do mesmo
    tamanho
    '''
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
    






        







    


    
