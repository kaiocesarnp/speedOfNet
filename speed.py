# Speedtest-cli, utilitário de linha de comando para testar a velocidade da internet

import subprocess

def test_speed():
    speedtest_cmd = "speedtest-cli --bytes --simple"
    process = subprocess.Popen(speedtest_cmd.split(), stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output

output = test_speed()
print(output)

# Explicação de cada linha:

# import subprocess Esta linha importa o módulo subprocess, que permite a criação de processos 
                                # e a comunicação com eles a partir do código Python.

# def test_speed(): Esta linha define uma função chamada test_speed(), que será usada para executar um teste de velocidade de internet.

    # speedtest_cmd = "speedtest-cli --bytes --simple" Esta linha cria uma variável chamada speedtest_cmd que armazena a string "speedtest-cli --bytes --simple". 
                                                                    # Essa string é o comando que será passado para o processo subprocesso 
                                                                    # para executar o teste de velocidade usando a ferramenta de linha de comando 
                                                                    # speedtest-cli, que é uma biblioteca popular para medir a velocidade de internet em Python.


    # process = subprocess.Popen(speedtest_cmd.split(), stdout=subprocess.PIPE) Esta linha cria um objeto de processo subprocesso chamado process usando a função subprocess.Popen(). 
                                                                                # O primeiro argumento é uma lista de strings gerada pela função split() aplicada à variável speedtest_cmd, 
                                                                                # o que separa a string em palavras individuais. O argumento stdout=subprocess.PIPE especifica que a saída 
                                                                                # padrão do processo (ou seja, a saída que seria impressa no terminal) deve ser redirecionada para um 
                                                                                # objeto de tubo (pipe) para que possa ser lido pelo código Python.


    # output, _ = process.communicate() Esta linha chama o método communicate() no objeto de processo process, que espera o processo filho 
                                        # terminar de executar e captura sua saída. A saída do processo é retornada como uma tupla 
                                        # contendo a saída padrão e a saída de erro. Neste caso, a saída padrão é capturada e atribuída à 
                                        # variável output. O _ é uma convenção para descartar o valor da saída de erro, já que não está 
                                        # sendo usado neste código.

    # return output Esta linha retorna a saída capturada do processo, que será o resultado da função test_speed().

# output = test_speed() Esta linha chama a função test_speed() e atribui seu resultado à variável output.

# print(output) Esta linha imprime o valor da variável output, que contém a saída capturada do processo, 
                # ou seja, o resultado do teste de velocidade de internet.