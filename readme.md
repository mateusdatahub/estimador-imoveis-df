## 🏡 Estimativa de Preços de Imóveis no Distrito Federal

Este projeto apresenta um pipeline completo de **Ciência de Dados**, cobrindo desde a coleta e tratamento de dados imobiliários até a construção de um modelo de **Machine Learning** e sua aplicação prática em uma interface web interativa.

A proposta é explorar dados reais do mercado imobiliário do Distrito Federal, extrair padrões relevantes e utilizá-los para estimar o valor de imóveis com base em suas características.

## 🎯 Motivação

O mercado imobiliário apresenta alta variabilidade de preços, fortemente influenciada por fatores como `localização`, `área` e `número de quartos`.
Este projeto busca demonstrar como técnicas de Análise Exploratória de Dados e **Machine Learning** podem ser aplicadas para lidar com esse tipo de problema de forma estruturada e reproduzível.

## 📊 Fonte dos Dados

Os dados utilizados foram obtidos por meio de **web scraping** de anúncios públicos disponíveis na plataforma `DF Imóveis`, sendo utilizados exclusivamente para fins educacionais e analíticos.

Durante o processo, foram enfrentados desafios comuns em dados reais, como:

- valores ausentes

- inconsistências

- ruído

- alta dispersão

## 🛠️ Estrutura do Projeto

```text
├── DATA
│   ├── raw/                         # Dados brutos, sem qualquer tratamento
│   └── processed/                   # Dados tratados e prontos para modelagem
│
├── MODELS
│   ├── treinados/                   # Modelos treinados (.joblib)
│   └── metadados/                   # Metadados dos modelos (features, métricas, versões)
│
├── NOTEBOOKS
│   ├── 01_data_cleaning.ipynb       # Limpeza e preparação inicial dos dados
│   ├── 02_eda_analise_exploratoria.ipynb
│   │                                 # Análise Exploratória de Dados (EDA)
│   └── 03_modelagem.ipynb           # Modelagem, validação e tuning de modelos
│
├── RESULTS                          # Resultados finais, gráficos e métricas
│
├── SCRIPTS
│   ├── scrapping/                   # Scripts de coleta de dados (web scraping)
│   
│
├── VENV                             # Ambiente virtual do projeto
```

## ➡️ Etapas do Projeto  
#### 1️ Coleta e Limpeza dos Dados

📓 `_data_cleasing.ipynb`

- Padronização de tipos

- Tratamento de valores ausentes

- Correção de inconsistências

- Preparação do dataset final
- 
#### 2️ Análise Exploratória (EDA)

📓 `02_eda_analise_exploratoria.ipynb`

- Estatísticas descritivas

- Análise de distribuição e assimetria

- Avaliação da influência de área, quartos e localização

- Identificação de padrões do mercado

#### 3️ Modelagem Preditiva

📓 `03_modelagem.ipynb`

- Definição da variável alvo (LOG_VALOR_M2)

- Pipeline de pré-processamento

- Avaliação de diferentes modelos

- Validação cruzada

- Análise de métricas (R², MAE, RMSE)

✔️ Modelo final: **Random Forest Regressor**, escolhido por robustez e
desempenho frente à variabilidade dos dados.

## 🚀 Aplicação Web

O modelo treinado foi integrado a uma aplicação web desenvolvida em Streamlit, permitindo a interação direta com o usuário e a visualização prática dos resultados.

📄 Veja detalhes no README específico do app.

## 🌐 Aplicação Online
https://estimador-imoveis-df-vbrdam8od8harizn2dvond.streamlit.app/

## 🧑🏻‍💻 Tecnologias Utilizadas

- Python

- Pandas / NumPy

- Scikit-learn

- Plotly

- Streamlit

- Jupyter Notebook

## 😁 Autor

Mateus

Projeto desenvolvido para fins de portfólio em **Ciência de Dados** e **Machine Learning**.
