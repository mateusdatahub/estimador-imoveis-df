## 🏡 Estimador de Preços de Imóveis — Aplicação Web

Esta aplicação web foi desenvolvida com Streamlit e utiliza um modelo de **Machine Learning** previamente treinado para estimar o valor de imóveis no `Distrito Federal`.

Ela representa a camada final do projeto, conectando o modelo ao usuário de forma simples, visual e interativa.

## 🎯 O que a aplicação faz

#### A aplicação permite que o usuário:

- **Informe**:

    - Área do imóvel (m²)

    - Número de quartos

    - Bairro

- **Receba**:

    - Estimativa do valor por metro quadrado

    - Estimativa do valor total do imóvel

- **Visualize**:

    - Comparação com a distribuição real do mercado

    - Posicionamento do imóvel em relação aos demais anúncios

## 📊 Modelo Utilizado

- Algoritmo: **Random Forest Regressor**

- Variável alvo: `LOG_VALOR_M2`

- Métricas exibidas na aplicação:

    - R² (conjunto de teste)

    - MAE

    - RMSE

As métricas são carregadas dinamicamente a partir de um arquivo de metadados gerado durante a fase de modelagem.

## 🛠️ Estrutura Interna

- `models/Treinados/`: modelo serializado (`.joblib`)

- `models/metadados/`: métricas e informações do treinamento

- `data/processed/`: dados utilizados para comparação com o mercado

A aplicação utiliza cache inteligente do Streamlit para otimizar desempenho e carregamento.

## ▶️ Como Executar a Aplicação
```
streamlit run app.py
```
Certifique-se de que o modelo treinado e os arquivos de metadados estejam corretamente posicionados conforme a estrutura do projeto.

## ⚠️ Observações

- As estimativas são baseadas em padrões históricos do mercado

- O resultado não substitui uma avaliação imobiliária profissional

- O objetivo principal é educacional e analítico