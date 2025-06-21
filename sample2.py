"""Bu modül iki sayının toplamını hesaplayan bir fonksiyon içerir."""
def add(number1, number2):
    """İki sayıyı toplar ve sonucu döndürür.
    Args:
        number1 (int): İlk sayı.
        number2 (int): İkinci sayı.
    Returns:
        int: İki sayının toplamı.
    """
    return number1 + number2

NUM1 = 4

NUM2 = 5

TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
