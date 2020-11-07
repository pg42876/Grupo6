def tranforma():
    '''
    Função resposável por receber um ficheiro
    e de dar return de uma sequência em string
    '''
    filename = input ("filename: ")
    my_file = open(filename)
    my_file = my_file.readline()
    return(my_file)

