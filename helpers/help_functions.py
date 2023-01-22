def price_extractor(raw_string_with_price):
    return ''.join(s for s in raw_string_with_price if s.isdigit() or s == '.')
