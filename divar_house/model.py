from sklearn.ensemble import RandomForestRegressor

def build_model():
    
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=1
    )
    
    return model