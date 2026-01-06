# Number to Words Converter

A elegant and efficient Python solution to convert numerical values into their word representations. Perfect for generating readable text from numbers in applications like invoice generation, report writing, or any system requiring human-readable number formatting.

---

## 🎯 Features

- **Wide Range Support**: Converts numbers from 0 to 999,999,999,999 (up to trillions)
- **Clean Output**: Generates properly formatted, human-readable text
- **Recursive Algorithm**: Efficient implementation using recursive decomposition
- **Well-Tested**: Comprehensive test suite with multiple edge cases
- **Type Hints**: Fully annotated code for better IDE support and type safety
- **Easy Integration**: Simple function interface for easy integration into other projects

---

## 📋 Requirements

- Python 3.7 or higher

---

## 🚀 Installation

Simply download or copy the `src/` folder to your project directory. No external dependencies required! The project uses only Python standard library.

**Quick Setup:**
```bash
# Navigate to the src directory
cd src/
```

---

## 💡 Usage

### Basic Example

```python
from main import num_to_word

# Convert a number to words
result = num_to_word(127643)
print(result)
# Output: One hundred twenty Seven thousand Six hundred forty Three

result = num_to_word(9)
print(result)
# Output: Nine

result = num_to_word(0)
print(result)
# Output: Zero
```

### Supported Number Ranges

The function handles the following magnitudes:

| Range | Example | Output |
|-------|---------|--------|
| 0-19 | `num_to_word(15)` | `Fifteen` |
| 20-99 | `num_to_word(42)` | `forty Two` |
| 100-999 | `num_to_word(256)` | `Two hundred fifty Six` |
| 1,000+ | `num_to_word(1,234)` | `One thousand Two hundred thirty Four` |
| 1,000,000+ | `num_to_word(1,000,000)` | `One million` |
| 1,000,000,000+ | `num_to_word(1,000,000,000)` | `One billion` |
| 1,000,000,000,000+ | `num_to_word(1,000,000,000,000)` | `One trillion` |

---

## 📁 Project Structure

```
.
├── README.md                 # This file
├── src/
│   ├── main.py              # Core module with num_to_word() function
│   ├── constants.py         # Constants for numbers and word mappings
│   ├── main.ipynb           # Jupyter notebook with examples
│   └── __pycache__/         # Python cache directory
```

### File Descriptions

- **main.py**: Contains the `num_to_word()` function that performs the number-to-word conversion
- **constants.py**: Defines lookup dictionaries and lists for:
  - `UNDER_20`: Words for numbers 0-19
  - `TENS`: Words for tens (20, 30, 40, etc.)
  - `ABOVE_100`: Words for larger magnitudes (hundred, thousand, million, etc.)

---

## 🧪 Testing

The project includes built-in tests. Run the tests with:

```bash
python src/main.py
```

Expected output:
```
All tests passed.
```

### Test Cases Covered

- Single-digit numbers (0-9)
- Teens (10-19)
- Tens and combinations (20, 21, 99)
- Hundreds
- Thousands with full breakdown (127,643)

---

## 🔧 How It Works

The algorithm uses a **recursive decomposition** approach:

1. **Base Cases**: Numbers 0-19 are looked up directly from `UNDER_20`
2. **Tens Place**: Numbers 20-99 extract the tens digit from `TENS` and recursively add the ones place
3. **Larger Numbers**: For numbers ≥ 100, find the largest magnitude (hundred, thousand, million, etc.) that fits the number, then recursively process the quotient and remainder

**Example**: Converting 127,643
```
127643 → One hundred twenty Seven thousand Six hundred forty Three
  ├── 127 thousands → "One hundred twenty Seven"
  ├── 643 ones → "Six hundred forty Three"
  └── Combine with "thousand"
```

---

## 📊 Algorithm Complexity

- **Time Complexity**: O(log n) where n is the input number
- **Space Complexity**: O(log n) due to recursion depth

---

## 💬 Function Signature

```python
def num_to_word(num: int) -> str:
    """
    Convert a number to its word representation.
    
    Args:
        num (int): The number to convert (0 to 999,999,999,999)
    
    Returns:
        str: The word representation of the number
    
    Examples:
        >>> num_to_word(127643)
        'One hundred twenty Seven thousand Six hundred forty Three'
        >>> num_to_word(0)
        'Zero'
    """
```

---

## 📝 Notes

- The output capitalizes the first letter of major components (e.g., "One", "Twenty")
- Lowercase letters are used for compound numbers (e.g., "twenty" in "twenty One")
- The function is deterministic and will always produce the same output for the same input
- Maximum supported value: 999,999,999,999 (just under 1 trillion)

---

## 🚢 Use Cases

- **Invoice & Bill Generation**: Display monetary amounts in written form
- **Report Writing**: Embed readable numbers in generated documents
- **Accessibility**: Convert numbers for text-to-speech applications
- **Data Processing**: Transform numerical data to text format
- **Educational Projects**: Learn algorithm design and recursion patterns


---

## 📄 License

This project is provided as-is for educational purposes. Feel free to use and modify it according to your needs.

---

## 🤝 Contributing

Contributions are welcome! To improve the project:

1. Test edge cases
2. Optimize the algorithm
3. Extend support beyond trillions
4. Add internationalization (convert to other languages)
5. Submit suggestions and improvements

---

## 📞 Support

If you encounter any issues or have questions, please open an issue or contact the project maintainer.

---

## 🎓 Learning Resources

This project demonstrates:
- Recursive algorithm design
- String manipulation in Python
- Use of constants and lookup tables
- Type hints and documentation
- Test-driven development practices
