def tranforma(filename):
    '''
    Função responsável por receber um ficheiro
    e de dar return de uma sequência em string
    '''
    my_file = open(filename)
    my_file = my_file.readline()
    return(my_file)

def FASTARead(filename):
    '''
    Função responsável por receber um ficheiro FASTA e
    devolve uma sequência
    '''

    with open(filename, 'r') as readfile:
        seq = readfile.readlines()[1:]
        seq = [x.replace('\n', '') for x in seq]
        seq = ''.join(seq)
    return(seq)

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
    seq_trans = seq.replace('A', 'u').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return (seq_trans)

def traducao(cadeiaDNA):
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

def validarseq(seq):
    '''
    Função responsável por verificar 
    se uma sequência é válida ou não
    '''
    seq = seq.upper()
    if len(set(seq) - {'A','C','G','T'})==0:
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

    def traduz(seq):
        import re
        seq = re.findall('...', seq)

        l = []

        for x in seq:
            l.append(gencode[x])

        result = "".join(l)
        return (result)
    
    seq = seq.upper()  

    for a in range(3):
        return (traduz(seq[a:]))

    seq1 = seq[::-1]
    seq1 = seq1.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()

    for a in range(3):
        return (traduz(seq1[a:]))

def proteins(seq):
    '''
    Função que devolve a lista de todas
    as proteínas ordenadas por tamanho e 
    por ordem alfabética para as do mesmo
    tamanho
    '''
    seq = seq.upper()
    import re
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

    def traducao(seq):
        proteina = []
        for i in range(3):
            traducao = []
            sequencia = re.findall('...', seq[i:])
            for x in sequencia:
                traducao.append(gencode[x])
            traducao = "".join(traducao)
            proteina.extend(re.findall('M.*?_', traducao))
        return(proteina)
    
    def customkey(protein):
        return -len(protein), protein
    
    protein = []
    protein = traducao(seq)
    
    protein = list(dict.fromkeys(protein))

    protein = sorted(protein, key = customkey)
    print("\n".join(protein))
    
    
    
    
    


        







    


    
