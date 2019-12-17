# Importações
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

# Função Main a ser executada

# Apenas Um Aviso para caso as importações deem errado

# Variaveis Globais - Estas Variaveis alteram todos os valores

tempo_maximo = 45000
frequencia_mensagem = 5
frequencia_portadora = 40
amplitude_portadora = 1

# Vai dividir cada valor do vetor criado para que se obtenha valores pequenos
tempo = np.arange(tempo_maximo) / tempo_maximo
mensagem = np.sin(2 * np.pi * frequencia_mensagem * tempo)
portadora = np.multiply(amplitude_portadora, np.cos(
    2 * np.pi * frequencia_portadora * tempo))
modulado = np.multiply(mensagem, portadora)

# ---------------------------- Demodulação -------------------------------------

demodulado = np.multiply(modulado, portadora)

fc = 30
w = fc / (tempo_maximo / 2)
a, b = scipy.signal.butter(5, w, 'low')

demodulado = scipy.signal.filtfilt(a, b, demodulado)

# --------------------------- Gerar Graficos -----------------------------------

# Gráfico da Mensagem
plt.subplot(2, 2, 1)
plt.title('Mensagem')
plt.plot(mensagem)
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)

# Gráfico da Portadora
plt.subplot(2, 2, 2)
plt.title('Portadora')
plt.plot(portadora)
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)

# Gráfico do sinal final
plt.subplot(2, 2, 3)
plt.title('Sinal Modulado')
plt.plot(modulado)
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)

# Sinal Demodulado
plt.subplot(2, 2, 4)
plt.title('Sinal Demodulado')
plt.plot(demodulado)
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)

# Apresenta o Gráfico
plt.show()
