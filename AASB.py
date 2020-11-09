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
