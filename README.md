# Car Price Prediction

A machine learning project that predicts car prices using the K-Nearest Neighbors (KNN) algorithm.

## What it does

This project predicts car prices based on vehicle features. Given a car's specifications (Mileage, Make, Model, Trim, Type, Cylinder, Liter), it returns an estimated price along with evaluation metrics (MAE and RMSE).

## How it works

The `CarPricePredictor` class in `car_price_predicator.py` implements a KNN regression model:

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