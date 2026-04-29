# Credit Card Fraud Detection - Anomaly Detection Project

## Project Objective

The goal of this project is to identify unusual or suspicious patterns in credit card transaction data, such as transactions with abnormally high values, inconsistent durations, or atypical behaviors. Students will apply anomaly detection techniques (supervised or unsupervised) and evaluate the effectiveness of the models. This problem is particularly relevant in real-world contexts such as **fraud detection** or **data recording errors**.

### Key Learning Outcomes

- Apply supervised and unsupervised anomaly detection techniques
- Handle highly imbalanced datasets
- Evaluate model performance on financial transaction data
- Deal with outliers, noise, and temporal patterns in data

---

## Dataset Overview

**Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

This dataset contains credit card transactions made by European cardholders in September 2013. It presents transactions that occurred in 2 days, where there are 492 frauds out of 284,807 transactions (~0.17% fraud rate). The dataset is highly imbalanced, making it ideal for studying anomaly detection techniques.

### Dataset Characteristics

- **Total Transactions**: 284,807
- **Fraudulent Transactions**: 492 (0.17%)
- **Normal Transactions**: 284,315 (99.83%)
- **Data Type**: Structured tabular data with numerical features
- **Temporal Nature**: Time-series of sequential events
- **Financial Data**: Real transaction amounts in EUR

---

## Data Dictionary

### Columns Description

| Column | Type | Description |
|--------|------|-------------|
| **Time** | Integer | Number of seconds elapsed between this transaction and the first transaction in the dataset. Represents temporal sequence of events. |
| **V1 - V28** | Float | Principal Component Analysis (PCA) transformed features derived from the original transaction data. These 28 features are the result of dimensionality reduction applied to protect customer privacy. Each V<n> represents a transformed principal component. |
| **Amount** | Float | The transaction amount in EUR (Euro). This is the only feature that has not been normalized/transformed and represents the real monetary value. |
| **Class** | Integer | **Target variable for classification/anomaly detection**. Takes two values: <br> - `0`: Normal transaction <br> - `1`: Fraudulent transaction (anomaly) |

### Feature Details

#### Temporal Feature
- **Time**: Useful for understanding temporal patterns and sequences. Can be used to engineer time-based features like transaction frequency, velocity, or time-of-day patterns.

#### Anonymized Features (V1-V28)
- The original features were transformed using PCA to protect the sensitive nature of the data while maintaining their predictive power.
- **Why PCA?** Principal Component Analysis reduces dimensionality, removes correlated features, and preserves variance needed for anomaly detection.
- These features capture various aspects of transactions such as merchant information, transaction type patterns, and cardholder behavior.
- Ranges vary from approximately -50 to +25, centered around 0.

#### Transaction Amount
- **Amount**: This is the only original, untransformed feature. It ranges from 0 to over 25,000 EUR.
- Critical for understanding fraud patterns: fraudsters may target small or large amounts.
- Can have significant outliers which are important for anomaly detection.

#### Target Variable
- **Class**: Binary classification problem (0 = normal, 1 = fraud).
- This is what we aim to predict using anomaly detection techniques.
- The extreme imbalance (0.17% fraud rate) makes this a challenging dataset requiring special techniques.

---

## Data Challenges

1. **Class Imbalance**: Only 0.17% of transactions are fraudulent, making standard classification algorithms biased towards the majority class.
2. **Dimensionality**: 28 PCA-transformed features require careful interpretation and selection.
3. **Outliers and Noise**: Financial data often contains unusual values; distinguishing between fraud and legitimate outliers is critical.
4. **Temporal Dependency**: Transactions have a temporal sequence that may contain patterns.
5. **Feature Anonymization**: PCA-transformed features limit interpretation, but preserve privacy.

---

## Anomaly Detection Approaches

### Supervised Techniques
- Logistic Regression with class weights
- Random Forests
- Gradient Boosting (XGBoost, LightGBM)
- Neural Networks with custom loss functions

### Unsupervised Techniques
- Isolation Forest
- Local Outlier Factor (LOF)
- Autoencoders
- Clustering-based methods (K-Means)
- Statistical methods (Z-score, IQR)

### Evaluation Metrics
- **Precision**: Among detected frauds, how many are truly fraudulent?
- **Recall**: Among all frauds, how many did we detect?
- **F1-Score**: Harmonic mean balancing precision and recall
- **ROC-AUC**: Performance across all thresholds
- **PR-AUC**: Precision-Recall curve AUC (better for imbalanced data)
- **Confusion Matrix**: Detailed breakdown of predictions

---

## Project Structure

```
anomaly_detection_project/
├── data/
│   ├── creditcard.csv           # Main dataset
│
├── src/
│   ├── test_spark.py            # Spark-based data loading example
│   └── TODO 
├── README.md                     # This file
└── requirements.txt             # Python dependencies
```

---

## Getting Started

### 1. Download the Dataset
```bash
curl -L -o ~/anomaly_detection_project/data/creditcardfraud.zip \
  https://www.kaggle.com/api/v1/datasets/download/mlg-ulb/creditcardfraud

unzip creditcardfraud.zip
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Load and Explore the Data
```bash
python src/test_spark.py
```

---

## References

- **Dataset Paper**: [Creditcard Fraud Detection on Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **PCA Explanation**: Understanding Principal Component Analysis and its application to privacy protection in financial data
- **Anomaly Detection**: Chandola et al., "Anomaly Detection: A Survey", ACM Computing Surveys, 2009

---

**Project Status**: In Development  
**Last Updated**: April 2026
