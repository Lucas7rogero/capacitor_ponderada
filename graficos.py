import pandas as pd
import matplotlib.pyplot as plt
import io

dados_arduino = """
17646 2.10 2.90
18048 2.46 2.54
18448 2.38 2.62
18849 2.43 2.57
19251 2.41 2.59
19651 2.40 2.60
20052 2.40 2.60
20454 2.39 2.61
20855 2.39 2.61
21256 2.41 2.59
21657 2.44 2.56
22059 2.39 2.61
22459 2.39 2.61
22860 2.38 2.62
23262 2.38 2.62
23662 2.37 2.63
24064 2.18 2.82
"""

# PROCESSAMENTO DE DADOS

try:
    df = pd.read_csv(io.StringIO(dados_arduino), sep=' ',
                     names=['Tempo (ms)', 'Tensão R (V)', 'Tensão C (V)'],
                     comment='#')
    
    # Remove linhas vazias ou com erro, se houver
    df.dropna(inplace=True)

except Exception as e:
    print(f"Erro ao processar os dados. Verifique o formato copiado do Monitor Serial: {e}")
    exit()


# GERAÇÃO DOS GRÁFICOS
plt.figure(figsize=(10, 5))
plt.plot(df['Tempo (ms)'], df['Tensão C (V)'], color='blue', label='Tensão no C (V)')
plt.title('Carga/Descarga no Capacitor (C)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df['Tempo (ms)'], df['Tensão R (V)'], color='red', label='Tensão no R (V)')
plt.title('Tensão no Resistor (R)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df['Tempo (ms)'], df['Tensão C (V)'], color='blue', label='Tensão no C (V)')
plt.plot(df['Tempo (ms)'], df['Tensão R (V)'], color='red', label='Tensão no R (V)')
plt.title('Comparação: Carga/Descarga no C e Tensão no R')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.ylim(0, 5.2)
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
df['Soma V_C + V_R'] = df['Tensão C (V)'] + df['Tensão R (V)']
plt.plot(df['Tempo (ms)'], df['Soma V_C + V_R'], color='green', label='V_C + V_R')
plt.axhline(y=5.0, color='gray', linestyle='--', label='Tensão de Alimentação (5.0V)')
plt.title('Verificação da Lei das Malhas (V_C + V_R)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.show()