
Nosso CEO deseja saber algumas informações sobre o faturamento de vinhos. A equipe de vendas nos forneceu um dataset com alguns dados e precisamos extrair algumas informações para respondermos as questões



import pandas as pd

#puxando a base de dados
dataset = 'https://raw.githubusercontent.com/rafaelpuyau/infinity_school/main/ds/datasets/wines.csv'
df = pd.read_csv(dataset, parse_dates=['date'])
df

df.dtypes

df['date'] = df['date'].map(lambda dt: dt.strftime('%d/%m/%Y'))

df.sample(5)

## Perguntas do CEO

### 1. Quanto custa o vinho mais caro?

df['price'].max()


### 2. Quanto custa o vinho mais barato?

df['price'].min()

### 3. Qual o vinho mais caro?

df.loc[:'price'].max()

### 4. Qual o vinho mais barato?

df.loc[:'price'].min()

### 5. Quanto foi vendido em 2021?

df['sub-total'] = df['price']*df['quantity']
faturamento = f'R${df["sub-total"].sum():,.2f}'
faturamento

### 6. Quantas garrafas no total?

df['quantity'].sum()

### 7. Qual vinho teve a maior nota?

maior_n = df['rate'] == 100
df.loc[maior_n]

### 8. Qual vinho teve a menor nota?

#### Gabarito

menor_n = df['rate'] == 75
df.loc[menor_n]

### 9. Qual a safra mais antiga?

df['vintage'].min()

### 10. Qual a safra mais recente?

df['vintage'].max()

### 11. Qual país teve mais garrafas vendidas?

> Bloco com recuo



df.groupby('country')['quantity'].sum().sort_values(ascending=False).reset_index()[:1]

### 12. Qual país teve menos menos garrafa vendida?

df.groupby('country')['quantity'].sum().sort_values(ascending=True).reset_index()[:1]

### 13. Quantos vinhos abaixo de R$100,00 foram vendidos?

df[df['price']<100]['quantity'].sum()

### 14. Quantos vinhos acima de R$100,00 foram vendidos?

df[df['price']>100]['quantity'].sum()

### 15. Quantas garrafas de espumantes foram vendidadas no mês de Dezembro?

df['date'] = pd.to_datetime(df['date'])

df.loc[(df['style']=='Sparkling') & (df['date'].dt.month==12)]['quantity'].sum()

### 16. Quantos vinhos brancos e rosés

1.   Item - brancos
2.   Item - rosés

foram vendidos nos meses de Janeiro à Março?

df.loc[((df['style']=='White')|(df['style']=='Rose')) & (df['date'].dt.month.isin([1,2,3]))]['quantity'].sum()

### 17. Qual foi o faturamento do 1º trimestre de 2021?

df['sub-total'] = df['price']*df['quantity']
fat = df.loc[df["date"].dt.month<4]['sub-total'].sum()
fat