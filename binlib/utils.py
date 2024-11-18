def is_valid_binary(binary):
    return all(char in '01 ' for char in binary)

def clean_binary(binary):
    return ' '.join(filter(None, binary.split()))
    