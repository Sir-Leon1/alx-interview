# Making Change

## Description
This project involves creating a function that determines the minimum number of coins needed to make change for a given amount of money. The function will be implemented in Python.

## Requirements
- Python 3.x

## Function Prototype
```python
def make_change(coins, total):
    """
    Determines the minimum number of coins needed to make change for a given amount of money.

    Args:
        coins (list): A list of the values of the coins available.
        total (int): The total amount of money to make change for.

    Returns:
        int: The minimum number of coins needed to make change for the total amount.
             If change cannot be made, return -1.
    """
```

## Usage
To use the `make_change` function, you need to provide a list of coin values and the total amount of money for which you need to make change.

Example:
```python
coins = [1, 2, 5]
total = 11
print(make_change(coins, total))  # Output: 3 (5 + 5 + 1)
```

## Testing
You can test the function by running a Python script with various inputs to ensure it returns the correct minimum number of coins.

## Author
- Sir Leon

## License
This project is licensed under the MIT License.