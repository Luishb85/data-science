# 🏠 Short-Term Rental Price Prediction — Rio de Janeiro

A multiple linear regression project to predict short-term rental nightly prices in Rio de Janeiro, based on physical characteristics, location, guest ratings, and listing engagement.

Developed as part of my MBA studies in Data Science, AI & Analytics (USP ESALQ), applying multivariate analysis, variable selection, and statistical diagnostics in practice.

---

## 🎯 Objective

Build an interpretable model capable of explaining and predicting nightly rental prices in Rio de Janeiro's mid-market segment, using a public dataset of over 40,000 listings, covering the full data project lifecycle: cleaning, exploratory analysis, feature engineering, variable selection, modeling, and evaluation.

## 📊 About the data

A public dataset of short-term rental listings in Rio de Janeiro, containing information about property characteristics, location, host, availability, reviews, and price. The original dataset has approximately 48,700 records and 90+ columns.

**Scope:** the analysis was restricted to the mid-market rental segment (nightly rates up to R$3,000 and minimum stays up to 10 nights), excluding extreme luxury listings and long-term-stay cases, which fall outside the short-term rental profile.

## 🔍 What was done

### 1. Data cleaning and preparation
- Removed columns with 100% missing values and low-relevance fields (IDs, URLs, scraping metadata)
- Applied differentiated missing-value treatment per variable (imputation, row removal, or column removal, depending on the pattern and percentage of missingness)
- Handled outliers based on business criteria (percentiles) and data-consistency checks (e.g., removed 20 records with an implausible relationship between number of bedrooms and guest capacity)
- Reduced cardinality of categorical variables (`property_type`: 79 → 11 categories; `neighbourhood_cleansed`: 154 → 22 categories)

### 2. Exploratory data analysis
- Investigated the relationship between ratings, price, property type, and occupancy/vacancy
- Identified an optimal pricing "sweet spot" (R$200–400/night range showing the highest average occupancy)
- Key finding: highly rated listings (score ≥ 4.5) consistently show higher occupancy across all 15 most represented neighborhoods, also associated with more competitive pricing

### 3. Feature engineering
- Created `numero_amenities` (amenity count per listing)
- Applied target encoding for location (`bairro_score`) and property type (`property_type_score`), reducing dozens of dummy variables into two continuous variables with stronger predictive power
- Tested alternative hypotheses (ratios between variables, geographic distance to a reference point) — only features that added real predictive value were kept

### 4. Variable selection
- **VIF (Variance Inflation Factor):** confirmed the absence of problematic multicollinearity (maximum of 3.33, well below the reference threshold)
- **OLS regression (statsmodels):** removed statistically non-significant variables, validated with robust standard errors (HC3) given residual heteroscedasticity
- **Random Forest:** used as a cross-check on variable relevance via a non-linear method — for variable selection support only, not as the final model

### 5. Modeling and evaluation
- Final model: Multiple Linear Regression, 17 variables, all statistically significant
- Benchmarked against Lasso, Ridge, and Elastic Net (converging results, confirming no redundancy left to correct)
- Residual diagnostics (heteroscedasticity and normality) documented with interpretation caveats

**Result (test set):** R² ≈ 0.486 | RMSE ≈ 0.498 (log scale)

## 📁 Repository structure

```
├── 1 - airbnb_datacleaning.ipynb    # Cleaning, EDA, and feature engineering
├── 2 - modelo_aula_regressao.ipynb  # Modeling (course-based structure, adapted to this project's data)
├── 3 - airbnb_predict.ipynb         # Prediction pipeline using the trained model
├── models/                          # Saved model, scaler, and encoding maps (.pkl)
├── images/                          # Charts generated during analysis
├── data/                            # Raw and processed data
├── requirements.txt
└── README.md
```

> 💡 The notebook `2 - modelo_aula_regressao.ipynb` follows a course-based structure, adapted to the specific data and decisions of this project.

## 🧠 Key takeaways

- The difference between statistical significance and practical relevance of a variable (not every variable with p<0.05 has a meaningful business effect)
- Multicollinearity assessed jointly (VIF) is more reliable than only looking at pairwise correlations in a heatmap
- Regularized models (Lasso/Ridge) serve as independent validation of the quality of a manually performed variable selection
- A moderate R² (~0.49) in a linear model can be the expected and correct outcome when the modeled phenomenon has non-linear components — confirmed by comparison with Random Forest (R² ≈ 0.61)

## 🛠️ Tech stack

Python · pandas · NumPy · scikit-learn · statsmodels · seaborn · matplotlib

## 📌 Known limitations

- The model does not incorporate listing text, photo quality, or other subjective factors, which likely explain part of the price variance not captured
- The causal relationship between occupancy and price is not fully resolved by the model (it may be bidirectional)
- Location and property-type scores (target encoding) were calculated over the full dataset in this exploratory phase; for production use, they should be recalculated using training data only, to avoid data leakage

---

📫 [LinkedIn](#) — feel free to reach out or suggest improvements.
