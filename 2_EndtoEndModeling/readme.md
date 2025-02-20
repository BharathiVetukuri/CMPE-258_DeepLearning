# Complete End-to-End Modeling with Deep Learning 🧠💻

## 📝 Assignment:
As a part of this assignment, demonstrated three deep learning models in three separate Colab notebooks:
- **a) Classification**: https://colab.research.google.com/drive/1cYfiEYYcaFK45YGedTEWfA5ubM__0iXK?usp=sharing 
- **b) Regression**: https://colab.research.google.com/drive/1cdmizVufAfSoCFLxdGM7leMyBbJi4aP1?usp=sharing 
- **c) Image Classification**: https://colab.research.google.com/drive/1ikwkOApL-iHbqduoj0THOtQM_odiC-JD?usp=sharing 

### 🎥 Youtube Video:

https://youtu.be/VfKJ4rF0_08 

[![Modeling](https://img.youtube.com/vi/VfKJ4rF0_08/0.jpg)](https://www.youtube.com/watch?v=VfKJ4rF0_08) 

 
### 📊 Integration and Artifacts:
- Integrate with Weights & Biases (preferred) or TensorFlow TensorBoard.
- Provide all the artifacts and metrics as demonstrated in the class for each of the models:
  - **a) Classification Metrics:** Accuracy, Precision, Recall, F1 Score (per class and overall)
  - **b) Regression Metrics:** ROC and PR curves
  - **c) Image Classification Metrics:** Example images per class, per class error analysis, and all metrics

## 🚀 Integration with TensorFlow TensorBoard:

### 1. Classification

![image](https://github.com/user-attachments/assets/0c89271a-08a5-410b-af0a-55c7d3208589)

### 2. Regression

![image](https://github.com/user-attachments/assets/08d9934b-1ffc-4c3c-a34a-d4b97a76d0cc)


![image](https://github.com/user-attachments/assets/87f7d374-0e63-4ace-9ba6-3810aa3494dc)

### 3. Image Classification

![image](https://github.com/user-attachments/assets/ef87c8db-d1db-4e62-aff4-0000b4a86bb7)


![image](https://github.com/user-attachments/assets/02d11737-71e3-4274-b783-a0c7ff8bf272)

# 📌 Summary of Metrics & Artifacts

Here’s the updated table reflecting the improvements in the regression model using the **California Housing Prices dataset**:

| **Model**                      | **Accuracy, Precision, Recall, F1** | **ROC & PR Curves** | **Per-Class Examples** | **Error Analysis** |
|---------------------------------|-------------------------------------|---------------------|-----------------------|---------------------|
| **IMDB Sentiment (LSTM)**       | ✅ `classification_report()`        | ✅ `roc_curve()`    | ✅ Printed text examples | ✅ Confusion Matrix & error distribution |
| **California Housing (Regression)** | ✅ `mse`, `rmse`, `mae`, `r2_score` | ✅ Converted regression into classification for ROC/PR curves | ✅ Displayed per-sample predictions | ✅ Residual analysis, scatter plots, confusion matrix for binned price categories |
| **Fashion MNIST (CNN)**         | ✅ `classification_report()`        | ✅ `roc_curve()` for each class | ✅ Misclassified images displayed | ✅ Confusion Matrix & per-class error rate |



