# Island Perimeter

## Description
This project involves creating a function that calculates the perimeter of an island described in a grid. The function will be implemented in Python.

## Requirements
- Python 3.x

## Function Prototype
```python
def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list): A list of list of integers where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
```

## Usage
To use the `island_perimeter` function, you need to provide a grid representing the island.

Example:
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Testing
You can test the function by running a Python script with various inputs to ensure it returns the correct perimeter of the island.

## Author
- Sir Leon

## License
This project is licensed under the MIT License.
