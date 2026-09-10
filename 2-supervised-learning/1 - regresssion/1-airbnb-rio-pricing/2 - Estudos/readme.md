# 🏠 Previsão de Preços de Hospedagem — Rio de Janeiro

Projeto de regressão linear múltipla para prever o preço de diária de imóveis de temporada no Rio de Janeiro, com base em características físicas, localização, avaliação e engajamento do anúncio.

Desenvolvido como parte dos meus estudos de MBA em Data Science, AI & Analytics (USP ESALQ), aplicando na prática os conceitos de análise multivariada, seleção de variáveis e diagnóstico estatístico.

---

## 🎯 Objetivo

Construir um modelo interpretável capaz de explicar e prever o preço de diária de imóveis de temporada no mercado médio do Rio de Janeiro, a partir de um dataset público com mais de 40 mil anúncios, cobrindo todo o ciclo de um projeto de dados: limpeza, análise exploratória, engenharia de atributos, seleção de variáveis, modelagem e avaliação.

## 📊 Sobre os dados

Base pública de anúncios de hospedagem de temporada no Rio de Janeiro, contendo informações sobre características do imóvel, localização, host, disponibilidade, reviews e preço. Dataset original com ~48.700 registros e 90+ colunas.

**Recorte de escopo:** a análise foi delimitada ao mercado médio de hospedagem (diárias até R$3.000 e estadia mínima de até 10 noites), excluindo imóveis de luxo extremo e casos de temporada longa, que fogem do perfil de hospedagem de curta duração.

## 🔍 O que foi feito

### 1. Limpeza e tratamento de dados
- Remoção de colunas com 100% de valores ausentes e de baixa relevância (IDs, URLs, metadados de scraping)
- Tratamento diferenciado de valores ausentes por variável (imputação, remoção de linhas ou remoção de coluna, conforme o padrão e o percentual de ausência)
- Tratamento de outliers com base em critério de negócio (percentis) e em consistência física dos dados (ex: remoção de 20 registros com relação implausível entre número de quartos e capacidade do imóvel)
- Redução de cardinalidade de variáveis categóricas (`property_type`: 79 → 11 categorias; `neighbourhood_cleansed`: 154 → 22 categorias)

### 2. Análise exploratória
- Investigação da relação entre avaliação, preço, tipo de imóvel e ocupação/vacância
- Identificação de um "ponto ótimo" de precificação (faixa de R$200–400/diária com maior ocupação média)
- Achado central: imóveis bem avaliados (nota ≥ 4,5) apresentam ocupação consistentemente maior em todos os 15 bairros mais representativos da amostra, associada também a preços mais competitivos

### 3. Engenharia de atributos
- Criação de `numero_amenities` (contagem de comodidades por imóvel)
- Target encoding para localização (`bairro_score`) e tipo de imóvel (`property_type_score`), reduzindo dezenas de variáveis dummy a duas variáveis contínuas com maior poder preditivo
- Testes de hipóteses alternativas (razões entre variáveis, distância geográfica a ponto de referência) — mantidas apenas as que agregaram valor preditivo real

### 4. Seleção de variáveis
- **VIF (Variance Inflation Factor):** confirmação de ausência de multicolinearidade problemática (máximo de 3,33, bem abaixo do limiar de referência)
- **Regressão OLS (statsmodels):** remoção de variáveis estatisticamente não significativas, com validação via erros-padrão robustos (HC3) diante de heterocedasticidade residual
- **Random Forest:** validação cruzada da relevância das variáveis por um método não-linear, usado apenas como apoio à seleção — não como modelo de entrega

### 5. Modelagem e avaliação
- Modelo final: Regressão Linear Múltipla, 17 variáveis, todas estatisticamente significativas
- Validação comparativa com Lasso, Ridge e Elastic Net (resultados convergentes, confirmando ausência de redundância a corrigir)
- Diagnóstico de resíduos (heterocedasticidade e normalidade) documentado com ressalvas de interpretação

**Resultado (conjunto de teste):** R² ≈ 0,486 | RMSE ≈ 0,498 (escala logarítmica)

## 📁 Estrutura do repositório

```
├── 1 - airbnb_datacleaning.ipynb    # Limpeza, EDA e engenharia de atributos
├── 2 - airbnb_predict.ipynb         # Pipeline de predição com o modelo treinado
├── 3 - modelo_aula_regressao.ipynb  # Modelagem (estrutura de aula, adaptada aos dados do projeto)
├── models/                          # Modelo, scaler e mapas de encoding salvos (.pkl)
├── images/                          # Gráficos gerados durante a análise
├── data/                            # Dados brutos e processados
├── requirements.txt
└── README.md
```

> 💡 O notebook `2 - modelo_aula_regressao.ipynb` segue a estrutura de uma aula de curso, adaptada aos dados e decisões específicas deste projeto.

## 🧠 Principais aprendizados

- Diferença entre significância estatística e relevância prática de uma variável (nem toda variável com p<0,05 tem efeito relevante no negócio)
- Multicolinearidade avaliada de forma conjunta (VIF) é mais confiável do que só observar correlações par a par em um heatmap
- Modelos de regularização (Lasso/Ridge) servem como validação independente da qualidade de uma seleção de variáveis feita manualmente
- Um R² moderado (~0,49) em um modelo linear pode ser o resultado esperado e correto quando o fenômeno modelado tem componentes não-lineares — confirmado pela comparação com Random Forest (R² ≈ 0,61)

## 🛠️ Tecnologias

Python · pandas · NumPy · scikit-learn · statsmodels · seaborn · matplotlib

## 📌 Limitações conhecidas

- O modelo não incorpora informações textuais do anúncio, qualidade de fotos ou fatores subjetivos, que provavelmente explicam parte relevante da variância de preço não capturada
- Relação de causalidade entre ocupação e preço não é totalmente elucidada pelo modelo (pode ser bidirecional)
- Scores de bairro e tipo de imóvel (target encoding) foram calculados sobre o dataset completo nesta fase exploratória; para uso em produção, devem ser recalculados exclusivamente sobre dados de treino, evitando vazamento de dados

---

# Fonte

https://insideairbnb.com/pt/get-the-data/
listings.csv.gz -	Detailed Listings data

Rio de Janeiro
Data - 24 June, 2026