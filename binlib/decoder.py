def binary_to_text(binary):
    try:
        chars = binary.split()
        return ''.join(chr(int(b, 2)) for b in chars)
    except ValueError:
        raise ValueError("Некорректный бинарный код.")
        