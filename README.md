# 🚀 Cloud Data Pipeline: GCP + Terraform + Python

Este projeto demonstra a automação completa de uma infraestrutura de Business Intelligence na nuvem, desde o provisionamento do servidor até a carga automatizada de dados.

## 🛠️ Tecnologias e Ferramentas
* **Cloud**: Google Cloud Platform (GCP)
* **IaC**: Terraform (Infraestrutura como Código)
* **Banco de Dados**: PostgreSQL
* **Linguagem**: Python (Pandas & SQLAlchemy)
* **S.O.**: Debian Linux

## 🏗️ Arquitetura do Projeto
1. **Infraestrutura**: Provisionamento automatizado de uma VM no Google Compute Engine utilizando Terraform.
2. **Engenharia de Dados**: Configuração de um servidor PostgreSQL para armazenamento estruturado de métricas de BI.
3. **ETL Pipeline**: Script Python que realiza a extração de dados simulados, aplica regras de transformação (ajuste de valores) e carrega os dados automaticamente no banco de dados.

## 📊 Como Visualizar os Resultados
Após a execução da pipeline, os dados podem ser consultados via SQL:
`SELECT * FROM vendas;`