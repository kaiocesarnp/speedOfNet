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

# O módulo subprocess é importado para permitir a execução de comandos no sistema operacional a partir do código Python.
# A função test_speed() é definida para executar um teste de velocidade de internet.
# O comando de teste de velocidade é armazenado em uma variável chamada speedtest_cmd.
# Um processo subprocesso é criado usando subprocess.Popen(), passando o comando de teste de velocidade como argumento 
                        # e redirecionando a saída para um objeto de tubo (pipe).

# A saída do processo é capturada usando o método communicate() e é atribuída à variável output. 
# A saída do processo é retornada como uma tupla contendo a saída padrão e a saída de erro.
# O '_' é uma convenção para descartar o valor da saída de erro, já que não está sendo usado neste código.

# 'return output': Esta linha retorna a saída capturada do processo, que será o resultado da função test_speed().

# A função test_speed() retorna a saída capturada.
# A função test_speed() é chamada e seu resultado é atribuído à variável output.
# O valor da variável output é impresso na tela, que contém o resultado do teste de velocidade de internet.