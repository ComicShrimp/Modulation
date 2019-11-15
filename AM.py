# Importações
import matplotlib.pyplot as plt
import numpy as np

# Funções Importantes
def sinalBandaBase():
    return 1


def sinalPortadora():
    return 2


# Função Main a ser executada

# Apenas Um Aviso para caso as importações deem errado

# Variaveis Globais - Estas Variaveis alteram todos os valores

tempo_maximo = 4500
frequencia_moduladora = 1
frequencia_portadora = 10
indice_modulacao = 1

# Vai dividir cada valor do vetor criado para que se obtenha valores pequenos
tempo = np.arange(tempo_maximo) / tempo_maximo
mensagem = np.sin(2 * np.pi * frequencia_moduladora * tempo) * indice_modulacao
portadora = np.cos(2 * np.pi * frequencia_portadora * tempo)
modulado = np.multiply(mensagem, portadora)
demodulado = np.divide(modulado, portadora)

# Gerar Graficos

# Gráfico da Mensagem
plt.subplot(2, 2, 1)
plt.title('Mensagem')
plt.plot(mensagem)
plt.xlabel('Amplitude')
plt.ylabel('Tempo')
plt.grid(True)

# Gráfico da Portadora
plt.subplot(2, 2, 2)
plt.title('Portadora')
plt.plot(portadora)
plt.xlabel('Amplitude')
plt.ylabel('Tempo')
plt.grid(True)

# Gráfico do sinal final
plt.subplot(2, 2, 3)
plt.title('Sinal Modulado')
plt.plot(modulado)
plt.xlabel('Amplitude')
plt.ylabel('Tempo')
plt.grid(True)

# Sinal Demodulado
plt.subplot(2, 2, 4)
plt.title('Sinal Demodulado')
plt.plot(demodulado)
plt.xlabel('Amplitude')
plt.ylabel('Tempo')
plt.grid(True)

# Apresenta o Gráfico
plt.show()