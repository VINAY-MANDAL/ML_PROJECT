# 🏡 House Price Prediction (My ML Journey)

Welcome to my Machine Learning learning repository! This project is a hands-on implementation to learn the core concepts of Machine Learning, Data Analytics, and Predictive Modeling using Python. 

Since my local system has resource constraints, this entire project is built and executed using cloud-based infrastructure (**Google Colab / Kaggle**), showcasing how to leverage cloud GPUs/CPUs for heavy data tasks.

---

## 🚀 Project Overview
The goal of this project is to predict house prices based on various features like area, number of bedrooms, location, and age of the property. It covers the complete ML pipeline from scratch:
* **Data Ingestion:** Loading and understanding the housing dataset.
* **Data Cleaning:** Handling missing values and removing outliers.
* **Feature Engineering:** Converting categorical data into numerical data.
* **Model Training:** Implementing Regression algorithms to predict continuous values.
* **Evaluation:** Checking model accuracy using metrics like R-squared and Mean Absolute Error (MAE).

---

## 🛠️ Tech Stack & Tools Used
* **Language:** Python 3.x
* **Environment:** Google Colab / Jupyter Notebooks (Cloud-based execution)
* **Data Manipulation:** NumPy, Pandas
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning Framework:** Scikit-Learn

---

## 📁 Repository Structure
```text
├── Data/
│   └── housing_data.csv       # Dataset used for training
├── house_pricing_model.ipynb  # Main Jupyter Notebook with code
├── .gitignore                 # To ignore local virtual env (myenv/)
└── README.md                  # Project documentation (this file)
```

---

## 📈 Learning Log & Milestones
* **Day 1:** Set up the virtual environment, connected VS Code to Google Colab, and loaded the dataset using Pandas.
* **Day 2:** Explored data distribution using Seaborn plots (Histograms & Scatter plots).
* **Day 3:** Cleaned missing entries and applied One-Hot Encoding to categorical columns.
* **Day 4:** Split data into Train/Test sets and successfully trained a `LinearRegression` model using Scikit-Learn.

---

## ⚙️ How to Run This Project Locally/Cloud
1. Clone this repository:
   ```bash
   git clone github.com
   ```
2. Upload the `house_pricing_model.ipynb` to your **Google Colab** or **Kaggle** account.
3. Upload the dataset from the `Data/` folder.
4. Run the cells step-by-step!

---
*💡 "Every error in the terminal is just another step closer to mastering Machine Learning."*
