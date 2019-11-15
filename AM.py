# Importações
import matplotlib.pyplot as plt
import numpy as np

# Função Main a ser executada

# Variaveis Globais - Estas Variaveis alteram todos os valores

tempo_maximo = 45000
indice_modulacao = 1

frequencia_mensagem = 5
amplitude_mensagem = 1

frequencia_portadora = 40
amplitude_portadora = 1

# Vai dividir cada valor do vetor criado para que se obtenha valores pequenos
tempo = np.arange(tempo_maximo) / tempo_maximo

# Cria a onda da portadora e da mensagem
mensagem = np.sin(2 * np.pi * frequencia_mensagem * tempo)
portadora = np.cos(2 * np.pi * frequencia_portadora * tempo)

# Implementa a equção: s(t) = Ac * [1 + Ka * m(t)] * cos(2 * pi * fc * t)
modulado = np.multiply(np.multiply(amplitude_portadora, np.add(
    indice_modulacao, np.multiply(amplitude_mensagem, mensagem))), portadora)

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

# Apresenta o Gráfico
plt.show()
