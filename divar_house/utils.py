def clean_price(value):
    if isinstance(value,str):
        value = value.replace("تومان","")
        value = value.replace("٬", "")
        value = value.replace(",", "")
        value = value.strip()
        
    return float(value)

def extract_city(address):
    # example تهران -> tehran
    
    if not isinstance(address, str):
        return "unknown"
    
    if "تهران" in address:
        return "tehran"
    
    return "other"