from car_price_predicator import CarPricePredicator

def main():
    predicator = CarPricePredicator(
        excel_file="./cars_data.xls"
    )
    
    predicator.fit()
    predicator.evaluate()
    
    print("\n Price Prediction \n")
    
    car = {
        "Mileage": 120000,
        "Make": "Toyota",
        "Model": "Corolla",
        "Trim": "LE",
        "Type": "Sedan",
        "Cylinder": 4,
        "Liter": 1.8
    }
    
    predicted_price = predicator.predict(car)
    print(
        f"Predicted price : ${predicted_price:,.2f}"
    )
    
if __name__ == "__main__":
    main()