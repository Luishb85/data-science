# Clustering for Fraud Detection — Unsupervised Learning Practice Project

A hands-on project testing whether unsupervised clustering can, on its own, uncover
transaction fraud patterns — without ever using the fraud label during training.

Built as a practical exercise while studying unsupervised learning techniques
(MBA in Data Science, AI & Analytics).

## Business Question

Fraud prevention teams often rely on fixed rules (e.g., "amount > X and outside
business hours = flag"). This project asks a different question: **without using
the fraud label at any point in training, can clustering discover a structure in
the data that already concentrates fraud into a small number of points — either
as a cluster, or as an anomaly?**

The `is_fraud` label is held out from every model and only revisited afterward,
for external validation — never for training.

## Dataset

[Fraud Detection](https://www.kaggle.com/datasets/waddahali/fraud-detection) (Kaggle) —
7,000 synthetic transaction records, deliberately built with:
- 10.3% class imbalance (fraud vs. legitimate)
- Missing data across all feature columns (2%–15% per column)
- 12 features: transaction amount, hour of day, weekend flag, item count, customer
  age, prior transaction count, distance from home, device type, network quality,
  first-transaction flag, store type, and a velocity score

This is a **synthetic, publicly available dataset** — no real institution's data
is involved.

## Methodology

Each data-treatment decision was made deliberately, with the end use (clustering,
not classification) in mind — several choices differ from what would be standard
for a supervised model.

### 1. Missing values (56.1% of rows affected)
- **Diagnosis:** missingness is MCAR (Missing Completely At Random) — no material
  relationship with fraud, no correlation between which columns go missing together.
- **Technique:** random sample imputation (drawing missing values from each column's
  own observed distribution), not median/mean imputation.
- **Why not median:** filling with a single fixed value stacks hundreds of points at
  the same coordinate, creating artificial density — a direct problem for a
  density-based algorithm like DBSCAN. Random sampling preserves the column's real
  distribution instead.
- **Why not KNN/MICE:** those techniques exploit correlation between features to
  impute more precisely — but the correlation matrix showed the features are
  essentially independent of one another, so the added complexity would buy little.

### 2. Outliers
- **Decision: kept, not removed or capped.** For a fraud-detection use case, an
  outlier (unusually high amount, unusual distance from home) is a candidate signal,
  not noise to clean away.
- **Scaling adjustment instead:** `RobustScaler` in place of `StandardScaler` — uses
  median and IQR rather than mean and standard deviation, so scaling isn't distorted
  by the very outliers the project deliberately preserved.

### 3. Feature selection for clustering
- Binary/categorical/low-cardinality variables (`is_weekend`, `device_type`,
  `is_first_transaction`, `store_type`, `hour_of_day`) were **excluded from the
  distance calculation**, since Euclidean distance treats their discrete jumps
  (0→1, or an arbitrary category order) as disproportionately large steps. This
  was confirmed empirically: an earlier run showed cluster separation dominated by
  `store_type` and `is_first_transaction` rather than the continuous variables.
- These columns are **not discarded** — they remain in the dataset to characterize
  and validate clusters after they're formed.
- Clustering ran on 7 genuinely continuous features: `transaction_amount`,
  `num_items`, `customer_age`, `prev_transactions`, `distance_from_home`,
  `network_quality`, `velocity_score`.

## Models Tested

| Model | Configuration | Validation metric | Result |
|---|---|---|---|
| K-Means | k=3, full feature set (incl. binaries), `StandardScaler` | ARI / NMI | ≈ 0.0055 / 0.0002 — null |
| K-Means | k=2, refined feature set, `RobustScaler` | ARI / NMI | -0.0001 / 0.0000 — null |
| DBSCAN | eps=1.2, min_samples=20 (grid-searched) | Lift / Recall | 1.31x / 9.7% — moderate signal |

k for K-Means was chosen with the Elbow method + Silhouette score; k=2 was the
statistically best silhouette, and was kept over a locally-better k=4 reading based
on a documented business trade-off (interpretability of a 2-segment split), not a
metric-reading error.

DBSCAN's `eps` was chosen via the k-distance graph, then validated with a grid
search across `eps` (0.9–1.6) and `min_samples` (10/14/20), measuring lift (fraud
rate inside noise ÷ overall fraud rate) and recall (% of real fraud captured as
noise) for each combination — not a single manually-picked value.

## Findings

1. **Fraud is not a cluster.** Two independent K-Means attempts, with materially
   different data treatments, both produced partitions statistically independent
   of real fraud. Getting the same null result twice, under different
   configurations, strengthens the conclusion rather than suggesting a
   configuration error.

2. **Fraud behaves a bit more like an anomaly — but the signal is moderate, not
   strong.** Treating fraud as noise (DBSCAN) rather than forcing it into a
   cluster produced the first real signal in the project: a 31% lift in fraud
   concentration within the "noise" group. It captures under 10% of actual fraud
   cases — nowhere near sufficient as a standalone detection tool.

3. **The limitation likely sits in the data, not the technique.** The correlation
   matrix showed the features are nearly independent of each other from the start
   — consistent with fraud being generated, in this synthetic dataset, from a few
   pointwise rules (high amount, unusual hour, first-time user) plus random noise,
   rather than a coherent multivariate pattern.

## Business Takeaway

This project **did not produce a production-ready fraud classifier** — and that is
a legitimate, useful conclusion, not a weak result. In a real compliance context,
this is exactly the kind of finding that prevents a team from investing time trying
to solve fraud detection with pure clustering, when a supervised model (using
`is_fraud` as the target) or more specific anomaly-detection techniques (Isolation
Forest, Autoencoders) would be the more appropriate path.

The value delivered here was different: a structured, honest test of three
unsupervised learning approaches, with justified data treatment at every step,
formal external validation instead of visual reading, and a result that resists
the temptation to force a positive conclusion where the numbers don't support one.

## Possible Next Steps (out of scope for this project)
- Test Isolation Forest or One-Class SVM as anomaly-detection alternatives better
  suited to this kind of dispersed pattern
- Benchmark against a supervised model (Logistic Regression, Random Forest) using
  `is_fraud` directly, to gauge how much signal actually exists in the data when
  the label is used
- Additional feature engineering (e.g., amount-to-history ratios) that might
  capture patterns the original variables don't, in isolation

## Stack

Python, pandas, NumPy, scikit-learn (`KMeans`, `DBSCAN`, `RobustScaler`,
`silhouette_score`, `adjusted_rand_score`, `normalized_mutual_info_score`),
seaborn, matplotlib.

## Repository Contents

- `Projeto_Fraude_Fase1.ipynb` — baseline K-Means notebook (Phase 1)
- `fraud.csv` — source dataset (Kaggle, synthetic)
- `README.md` — this file
