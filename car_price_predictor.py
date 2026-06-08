import pandas as pd
import numpy as np


class CarPricePredictor:

    def __init__(self, excel_file: str, k: int = 5):
        self.excel_file = excel_file
        self.k = k

        self.df = None
        self.feature_columns = None
        self.numeric_columns = [
            "Mileage",
            "Cylinder",
            "Liter"
        ]

        self.X = None
        self.y = None

        self.means = None
        self.stds = None

    def load(self):

        self.df = pd.read_excel(self.excel_file)

        required_columns = [
            "Price",
            "Mileage",
            "Make",
            "Model",
            "Trim",
            "Type",
            "Cylinder",
            "Liter"
        ]

        missing = [
            c
            for c in required_columns
            if c not in self.df.columns
        ]

        if missing:
            raise Exception(
                f"Missing columns: {missing}"
            )

        self.df = self.df.dropna()

    def prepare(self):

        X = self.df.drop(columns=["Price"])

        X = pd.get_dummies(
            X,
            columns=[
                "Make",
                "Model",
                "Trim",
                "Type"
            ],
            dtype=float
        )

        self.feature_columns = X.columns.tolist()

        self.means = X[self.numeric_columns].mean()
        self.stds = X[self.numeric_columns].std()

        self.stds = self.stds.replace(0, 1)

        X[self.numeric_columns] = (
            X[self.numeric_columns] - self.means
        ) / self.stds

        self.X = X.values.astype(np.float64)
        self.y = self.df["Price"].values.astype(np.float64)

    def fit(self):
        self.load()
        self.prepare()

    def build_feature_vector(self, car):

        row = pd.DataFrame([car])

        row = pd.get_dummies(
            row,
            columns=[
                "Make",
                "Model",
                "Trim",
                "Type"
            ],
            dtype=float
        )

        row = row.reindex(
            columns=self.feature_columns,
            fill_value=0
        )

        row[self.numeric_columns] = (
            row[self.numeric_columns] - self.means
        ) / self.stds

        return row.values.astype(np.float64)

    def predict(self, car):

        x = self.build_feature_vector(car)

        distances = np.sqrt(
            np.sum(
                (self.X - x) ** 2,
                axis=1
            )
        )

        nearest_indices = np.argsort(
            distances
        )[:self.k]

        nearest_prices = self.y[
            nearest_indices
        ]

        prediction = np.mean(
            nearest_prices
        )

        return round(float(prediction), 2)

    def evaluate(self):

        predictions = []

        for i in range(len(self.X)):

            current = self.X[i]

            distances = np.sqrt(
                np.sum(
                    (self.X - current) ** 2,
                    axis=1
                )
            )

            distances[i] = np.inf

            nearest = np.argsort(
                distances
            )[:self.k]

            pred = np.mean(
                self.y[nearest]
            )

            predictions.append(pred)

        predictions = np.array(predictions)

        mae = np.mean(
            np.abs(predictions - self.y)
        )

        rmse = np.sqrt(
            np.mean(
                (predictions - self.y) ** 2
            )
        )

        print(f"MAE  : {mae:,.2f}")
        print(f"RMSE : {rmse:,.2f}")