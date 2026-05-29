import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


def main():
    df = pd.read_csv("datasets/housing/housing.csv")
    housing = df.copy()

    housing_num = housing.drop("ocean_proximity", axis=1)
    num_attribs = list(housing_num.columns)
    cat_attribs = ["ocean_proximity"]

    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("std_scaler", StandardScaler()),
    ])

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    housing_prepared = full_pipeline.fit_transform(housing)
    print("prepared shape:", housing_prepared.shape)


if __name__ == "__main__":
    main()
