def from_decimal_convert(num: str, to_base: int) -> str:
    if not 2 <= to_base <= 36:
        raise ValueError("Base must be between 2 and 36")

    decimal_number = int(num)

    if decimal_number == 0:
        return "0"

    negative = decimal_number < 0
    decimal_number = abs(decimal_number)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while decimal_number > 0:
        res = digits[decimal_number % to_base] + res
        decimal_number //= to_base

    if negative:
        res = "-" + res
    return res

def to_decimal_convert(num: str, from_base: int) -> int:
    if not 2 <= from_base <= 36:
        raise ValueError("Base must be between 2 and 36")
    return int(num, from_base)