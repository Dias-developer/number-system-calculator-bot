def from_decimal_convert(num: str, to_base: int) -> str:
    decimal_number = int(num)
    if decimal_number == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while decimal_number > 0:
        res = digits[decimal_number % to_base] + res
        decimal_number //= to_base

    return res

def to_decimal_convert(num: str, from_base: int) -> int:
    return int(num, from_base)