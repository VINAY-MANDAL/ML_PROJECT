# Hands-On Machine Learning Journey 🚀

Welcome to my Machine Learning repository! This repo serves as my personal codebase, template center, and notebook journal as I master the concepts from the famous book **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron**.

The goal of this repository is to avoid reinventing the wheel—I document the implementation of pipelines, algorithms, and workflows chapter by chapter so that I can easily reuse these codebases as boilerplate templates for future real-world data science projects.

---

## 🛠️ Repository Structure & Chapters Covered

### 📁 Chapter 1: The Machine Learning Landscape
*   **Concepts:** Introduction to ML types (Supervised vs Unsupervised, Batch vs Online, Instance-based vs Model-based), main challenges of ML (insufficient data, non-representative data, overfitting, underfitting).
*   **Code Implementation:** Simple linear model training to predict life satisfaction based on GDP per capita.

### 📁 Chapter 2: End-to-End Machine Learning Project
*   **Concepts:** Frame the problem, look at the big picture, handle missing data, manage text/categorical attributes, feature scaling, and evaluate performance using Root Mean Squared Error (RMSE).
*   **Code Templates Built:**
    *   Stratified Shuffle Split (for unbiased train/test partitioning)
    *   Custom Data Preprocessing Pipelines (`Pipeline`, `ColumnTransformer`)
    *   Handling Missing Values (`SimpleImputer`) & Text Encoding (`OneHotEncoder`)
    *   Model Selection & Baseline Training (`LinearRegression`, `DecisionTreeRegressor`, `RandomForestRegressor`)

### 📁 Chapter 3: Classification
*   **Concepts:** Moving away from continuous regression to categorical classification using the MNIST digit dataset. Understanding the deep mechanics of model evaluation.
*   **Code Templates Built:**
    *   Stochastic Gradient Descent Classifier (`SGDClassifier`)
    *   Confusion Matrix, Precision, Recall, and F1-Score analysis
    *   The Precision/Recall Tradeoff visualization using `decision_function`
    *   Receiver Operating Characteristic (ROC) Curve and Area Under Curve (AUC) score computation
    *   Multiclass & Multilabel Classification setups

---

## 💡 How I Use This Repo (The Smart Workflow)
Rather than memorizing Scikit-Learn syntax, this repository acts as my custom reference manual. Whenever I face a new dataset:
1. I open my corresponding chapter folder or baseline template.
2. I copy the tested pipeline structural code.
3. I replace the dataset source and tweak hyper-parameters.
4. **Focus remains on Logic, Strategy, and Tuning, not syntax!**

---

## 👨‍💻 Developer Credit
*   **Developed and Maintained by:** Vinay Kumar Mandal  
*   **Language & Stack:** Python, Jupyter Notebooks, Scikit-Learn, Pandas, NumPy.

---
*Feel free to explore the notebooks! Every major block contains inline comments explaining the "Why" behind the code, matching my physical book annotations.*