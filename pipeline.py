import pandas as pd
from sqlalchemy import create_engine

# 1. EXTRACT: Criando dados de simulação de BI
novas_vendas = {
    'produto': ['Dashboard Power BI', 'Modelo Data Science', 'Infra Cloud Pro', 'Curso de SQL', 'teste vh'],
    'valor': [1500.00, 2800.00, 950.00, 500.00, 5000.00]
}
df = pd.DataFrame(novas_vendas)

# 2. TRANSFORM: Aplicando regra de negócio (10% de taxa)
df['valor'] = df['valor'] * 1.1

# Criando a coluna de data e hora atual
import datetime
df['data_carga'] = datetime.datetime.now()

# Criando um ID simples baseado na posição da linha
df['id'] = df.index + 1

# 3. LOAD: Enviando para o PostgreSQL no Google Cloud
# Nota: Em um projeto real, usaríamos variáveis de ambiente para a senha
engine = create_engine('postgresql://postgres:admin123@136.114.189.74:5432/bi_estudos')
df.to_sql('vendas', engine, if_exists='replace', index=False)

print("🚀 Sucesso! A pipeline carregou os dados no banco de dados.")