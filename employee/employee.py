import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'];

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx');
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0];
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0];
        print(f' \n Dos 3 mil dados cadastrados, '
              f'\n \nNo mês {mes} o seguinte funcionário bateu a meta:'
              f' \n Vendedor: {vendedor},'
              f' \n Vendas: {vendas}'
              f'\n Parabéns!!!');

#victorgeorges