# Car Price Prediction

A machine learning project that predicts car prices using the K-Nearest Neighbors (KNN) algorithm.

## What it does

This project predicts car prices based on vehicle features. Given a car's specifications (Mileage, Make, Model, Trim, Type, Cylinder, Liter), it returns an estimated price along with evaluation metrics (MAE and RMSE).

## How it works

The `CarPricePredictor` class in `car_price_predictor.py` implements a KNN regression model:

1. **Data Loading** - Reads car data from an Excel file (`cars_data.xls`) containing 804 vehicle records with columns: Price, Mileage, Make, Model, Trim, Type, Cylinder, Liter, Doors, Cruise, Sound, Leather

2. **Feature Preparation** - Converts categorical features (Make, Model, Trim, Type) into numeric vectors using one-hot encoding via `pd.get_dummies()`

3. **Normalization** - Scales numeric features (Mileage, Cylinder, Liter) by subtracting mean and dividing by standard deviation

4. **Prediction** - Uses k-nearest neighbors (default k=5) to find the closest matching cars in feature space and returns the average price of those neighbors

5. **Evaluation** - Calculates Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) using leave-one-out cross-validation

## K-Nearest Neighbors (KNN) Implementation

KNN is a simple, instance-based learning algorithm used here for regression:

- **Distance Calculation**: Uses Euclidean distance to measure similarity between cars in the normalized feature space
- **Neighbor Selection**: For prediction, finds the k=5 closest cars (nearest neighbors) to the input car
- **Prediction**: The predicted price is the mean of the prices of those k neighbors
- **Training**: No explicit training phase - the model simply stores all feature vectors
- **Cross-Validation**: The `evaluate()` method uses leave-one-out validation, where each car is predicted by finding neighbors among all other cars in the dataset

The key advantage of KNN is its simplicity and interpretability - predictions are based on actual similar cars from the dataset rather than learned parameters.

## API Reference

### `CarPricePredictor(excel_file: str, k: int = 5)`

Constructor that initializes the predictor with the path to the Excel data file and the number of neighbors (k).

### `__init__(self, excel_file: str, k: int = 5)`

Initializes the predictor with:
- `excel_file`: Path to the Excel file containing car data
- `k`: Number of nearest neighbors to use (default: 5)

### `load(self)`

Reads the Excel file into a pandas DataFrame and validates that required columns exist. Required columns: Price, Mileage, Make, Model, Trim, Type, Cylinder, Liter. Removes rows with missing values.

### `prepare(self)`

Prepares features for prediction:
- One-hot encodes categorical columns (Make, Model, Trim, Type)
- Normalizes numeric columns (Mileage, Cylinder, Liter) using z-score normalization
- Stores feature columns and scaling parameters (means, stds) for later use

### `fit(self)`

Convenience method that calls `load()` and `prepare()` in sequence.

### `build_feature_vector(self, car: dict) -> np.ndarray`

Converts a car dictionary into a normalized feature vector compatible with the training data:
- Applies one-hot encoding to categorical features
- Aligns features with training data columns (missing features filled with 0)
- Applies the same normalization used during training

### `predict(self, car: dict) -> float`

Predicts the price of a car:
- Builds feature vector using `build_feature_vector()`
- Computes Euclidean distances to all training samples
- Finds k nearest neighbors
- Returns the mean price of those neighbors

### `evaluate(self)`

Evaluates model performance using leave-one-out cross-validation:
- For each car, predicts price using neighbors from the rest of the dataset
- Calculates and prints MAE (Mean Absolute Error) and RMSE (Root Mean Squared Error)

## Usage

```bash
python main.py
```

The main script trains the model, evaluates it, and predicts the price of a sample Toyota Corolla with 120,000 miles and 1.8L 4-cylinder engine.

## Requirements

- pandas
- numpy
- xlrd (for Excel file reading)

## Files

- `main.py` - Entry point demonstrating the predictor
- `car_price_predictor.py` - CarPricePredictor class implementation
- `cars_data.xls` - Dataset with 804 car records