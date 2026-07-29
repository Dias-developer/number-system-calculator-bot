def to_decimal_convert(num: str, from_base: int, to_base: int) -> str:
    decimal_number = int(num, from_base)
    if decimal_number == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while decimal_number > 0:
        res += digits[decimal_number % to_base] + res
        decimal_number //= to_base

    return res