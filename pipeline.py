import pandas as pd
from sqlalchemy import create_engine

# 1. EXTRACT: Criando dados de simulação de BI
novas_vendas = {
    'produto': ['Dashboard Power BI', 'Modelo Data Science', 'Infra Cloud Pro'],
    'valor': [1500.00, 2800.00, 950.00]
}
df = pd.DataFrame(novas_vendas)

# 2. TRANSFORM: Aplicando regra de negócio (10% de taxa)
df['valor'] = df['valor'] * 1.1

# 3. LOAD: Enviando para o PostgreSQL no Google Cloud
# Nota: Em um projeto real, usaríamos variáveis de ambiente para a senha
engine = create_engine('postgresql://postgres:admin123@localhost:5432/bi_estudos')
df.to_sql('vendas', engine, if_exists='append', index=False)

print("🚀 Sucesso! A pipeline carregou os dados no banco de dados.")