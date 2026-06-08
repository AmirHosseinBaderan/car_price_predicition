import re

def to_english_digits(s):
    if not isinstance(s, str):
        return s

    persian = "۰۱۲۳۴۵۶۷۸۹"
    english = "0123456789"

    for p, e in zip(persian, english):
        s = s.replace(p, e)

    return s


def clean_price(value):

    if isinstance(value, str):

        # convert persian digits
        value = to_english_digits(value)

        # remove text and separators
        value = value.replace("تومان", "")
        value = value.replace("٬", "")
        value = value.replace(",", "")
        value = value.strip()

        # keep only numbers
        value = re.sub(r"[^\d]", "", value)

    try:
        return float(value)
    except:
        return None

def extract_city(address):
    # example تهران -> tehran
    
    if not isinstance(address, str):
        return "unknown"
    
    if "تهران" in address:
        return "tehran"
    
    return "other"

def clean_bool(x):
    if str(x).lower() in ["true", "1", "yes", "دارد"]:
        return 1
    return 0

def format_toman(value):
    """
    Convert numeric price to Persian Toman format
    Example:
    15524612878.78 → 15,524,612,879 تومان
    """

    try:
        value = int(round(float(value)))
    except:
        return "نامعتبر"

    # convert to Persian digits
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"

    def to_persian(num):
        s = str(num)
        result = ""
        for ch in s:
            if ch.isdigit():
                result += persian_digits[int(ch)]
            else:
                result += ch
        return result

    # format with commas
    formatted = f"{value:,}"

    # convert to Persian digits
    formatted = to_persian(formatted)

    return f"{formatted} تومان"