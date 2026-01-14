# Loan Default Risk Prediction System

**Multi-Stage AI System: Intelligent Prediction + Insight Engine**

---

## 1. Problem Statement

Financial institutions face significant losses due to loan defaults.
The objective of this project is to build an **end-to-end, production-thinking ML system** that predicts whether a borrower is likely to default on a loan.

The system:

- Uses **structured financial data** for core prediction
- Enhances prediction using **unstructured text data**
- Focuses on **error analysis, explainability, and deployment readiness**

This project is aligned with real-world risk modeling used in banking systems.

---

## 2. Dataset Description

**Source:** Kaggle – Lending Club Loan Dataset

### Target Variable

- `not.fully.paid`
  - `1` → Loan defaulted
  - `0` → Loan fully paid

### Structured Features (Examples)

- `fico` – Credit score
- `dti` – Debt-to-income ratio
- `int.rate` – Interest rate
- `installment` – Monthly EMI
- `revol.util` – Credit utilization
- `inq.last.6mths` – Recent credit inquiries

### Unstructured Feature

- `purpose` – Loan purpose (text)

### Data Characteristics

- Highly **imbalanced target**
- Financial outliers representing real high-risk borrowers
- No major missing values (validated)

---

## 3. Approach Overview

The system is built as a **multi-stage ML pipeline**:

1. Data understanding & EDA
2. Outlier handling and feature engineering
3. Text preprocessing and vectorization
4. Model training (baseline → advanced)
5. Model optimization and comparison
6. Error analysis & root cause analysis (RCA)
7. Model explainability (SHAP)
8. Deployment & scalability design

---

## 4. Feature Engineering

### Structured Feature Engineering

- **Outlier handling:** IQR-based capping (not removal)
- **Feature interactions:**
  - `income_to_installment`
  - `credit_utilization_risk`
- **Rationale:** Captures real borrower stress patterns better than raw features

### Feature Selection

- Correlation analysis
- Random Forest feature importance
- Business logic validation

---

## 5. Unstructured Data Integration (Text)

### Text Source

- `purpose` column

### Processing Steps

- Stopword removal
- TF-IDF vectorization
- Limited vocabulary for interpretability

### Why Text Helps

Text captures **borrower intent and motivation**, which structured financial data cannot express directly.
This improves discrimination between borderline safe and risky borrowers.

---

## 6. Models Built

Minimum three models were trained and evaluated:

1. **Logistic Regression** (Baseline)
2. **Random Forest** (Tree-based)
3. **Neural Network (MLP)** (Advanced)

### Model Optimization

- RandomizedSearchCV for Random Forest
- Overfitting controlled via depth and split constraints

---

## 7. Model Evaluation & Comparison

Metrics used:

- ROC-AUC
- Recall (priority metric)
- Precision
- F1-Score

**Best Model:** Tuned Random ForestChosen due to:

- Highest ROC-AUC
- Better recall (fewer false negatives)

---

## 8. Error Analysis & Root Cause Analysis (RCA)

### Key Focus

- **False Negatives** (predicted safe but defaulted)

### Observations

- Medium FICO but high DTI borrowers
- Ambiguous loan purposes
- Missing employment stability signals

### Business Impact

False negatives result in **direct financial loss**.

### Corrective Strategies

- Adjust decision threshold
- Increase FN penalty
- Add employment-related features

---

## 9. Model Explainability

### Techniques Used

- Random Forest feature importance
- SHAP global summary plot
- SHAP local explanation

### Outcome

- Model decisions align with financial risk logic
- Improves trust and regulatory explainability

---

## 10. Deployment & System Design

### API Framework

- **FastAPI**

### Deployment Flow

1. Receive JSON request
2. Validate input schema
3. Apply preprocessing (scaling, interactions, TF-IDF)
4. Generate default probability
5. Return risk label

### Cloud (AWS)

- S3 → model artifacts
- EC2 / ECS → FastAPI service
- CloudWatch → logging & monitoring
- IAM → access control

---

## 11. Performance & Scalability

- Batch scoring for large datasets
- Real-time inference via REST API
- Horizontal scaling using ECS
- Data drift and prediction drift monitoring
- Monthly retraining strategy
- Model versioning and rollback support

---

## 12. Learnings & Takeaways

- Feature engineering matters more than model complexity
- Error analysis provides more value than raw accuracy
- Text signals significantly enhance risk modeling
- Explainability is critical in financial ML systems
- Deployment thinking differentiates production ML from notebooks

---

## 13. Future Improvements

- Add employment history features
- Use embeddings or LLMs for richer text signals
- Cost-sensitive learning for FN reduction
- Automated drift detection pipelines

---

## Author

**Yash Gupta**
