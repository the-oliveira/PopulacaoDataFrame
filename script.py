import pandas as pd
import matplotlib.pyplot as plt

def plot_pop(filename, country_code):

    # reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # criando dataframe vazio
    data = pd.DataFrame()
    
    # iterando sobre os chunks do dataframe
    for df_urb_pop in urb_pop_reader:
        # Verificação para o código informado
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # zip nas informações necessárias para o código
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Total Urban Population %'])

        # transformando o zip em uma lista
        pops_list = list(pops)

        # Criando uma nova coluna no DataFrame 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
        
        # Concatenando o chunk do DataFrame no final de 'data'
        data = pd.concat([data, df_pop_ceb])

    # Plot
    data.plot(kind='bar', x='Year', y='Total Urban Population')
    plt.show()

