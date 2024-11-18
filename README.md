# binlib
### **README.md**

```markdown
# binary_library

`binary_library` is a Python library for working with binary code. It allows encoding text into binary code, decoding binary code into text, validating binary code, and cleaning binary code from unnecessary spaces.

## Installation

To install the library, download the project and run the following command:

```bash
pip install .
```

This command should be run in the folder where the `setup.py` file is located.

## Library Structure

- `binary_library/encoder.py`: functions for encoding text into binary code.
- `binary_library/decoder.py`: functions for decoding binary code into text.
- `binary_library/utils.py`: utilities for validating and cleaning binary code.
- `binary_library/__init__.py`: combines all modules for import.

## Usage

Once the library is installed, you can import the functions and use them in your code.

### Importing Functions

```python
from binary_library import text_to_binary, binary_to_text, is_valid_binary, clean_binary
```

### Usage Examples

#### 1. Encoding Text into Binary Code

Use `text_to_binary` to convert a text string into binary code.

```python
text = "Hello"
binary_code = text_to_binary(text)
print("Binary Code:", binary_code)
# Output: Binary Code: 01001000 01100101 01101100 01101100 01101111
```

#### 2. Decoding Binary Code into Text

Use `binary_to_text` to convert a binary code string back into text.

```python
binary_code = "01001000 01100101 01101100 01101100 01101111"
text = binary_to_text(binary_code)
print("Text:", text)
# Output: Text: Hello
```

#### 3. Validating Binary Code

Use `is_valid_binary` to check if a string is valid binary code (contains only `0`, `1`, and spaces).

```python
binary_code = "01001000 01100101 01101100 01101100 01101111"
is_valid = is_valid_binary(binary_code)
print("Valid Binary Code:", is_valid)
# Output: Valid Binary Code: True
```

#### 4. Cleaning Binary Code

Use `clean_binary` to remove unnecessary spaces from binary code.

``` python
binary_code = "01001000   01100101"
cleaned_binary_code = clean_binary(binary_code)
print("Cleaned Binary Code:", cleaned_binary_code)
# Output: Cleaned Binary Code: 01001000 01100101
```

## Errors and Exceptions

The `binary_to_text` function raises a `ValueError` if the binary code string is invalid and cannot be decoded.

``` python
try:
    binary_code = "01001000 0110010x ..."
    text = binary_to_text(binary_code)
except ValueError as e:
    print("Error:", e)
# Output: Error: Invalid binary code.
```
## License

This library is distributed under the MIT License. See the LICENSE file for more details.

# Tests
``` python
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```
