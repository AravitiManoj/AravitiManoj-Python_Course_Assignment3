# Assignment 3

This directory contains Python programs demonstrating basic programming concepts and the math module.

## Programs

### 1. Factorial.py
Calculates the factorial of a user-provided number using a for loop.

**Features:**
- Takes user input for a number
- Computes factorial using iterative multiplication
- Displays the result

**Usage:**
```bash
python Factorial.py
```

**Example:**
```
Enter a number: 5
Factorial of 5 is: 120
```

**Detailed Explanation:**

The factorial program calculates n! (n factorial), which is the product of all positive integers from 1 to n.

**Code Breakdown:**
1. **Line 1:** `factinput = int(input("Enter a number: "))`
   - Takes user input as a string
   - Converts it to an integer using `int()`
   - Stores the value in `factinput` variable

2. **Line 2:** `finalvalue = 1`
   - Initializes the result variable to 1
   - Starting with 1 is crucial because we'll be multiplying values
   - If we started with 0, the result would always be 0

3. **Lines 3-4:** `for i in range(1, factinput+1):`
   - Creates a loop that iterates from 1 to factinput (inclusive)
   - `range(1, factinput+1)` generates numbers: 1, 2, 3, ..., factinput
   - Each iteration multiplies `finalvalue` by the current number `i`
   - `finalvalue *= i` is shorthand for `finalvalue = finalvalue * i`

4. **Line 5:** `print(f"Factorial of {factinput} is: {finalvalue}")`
   - Uses an f-string to format and display the result
   - Shows both the input number and its calculated factorial

**Algorithm Flow:**
- For input 5:
  - Start: finalvalue = 1
  - i=1: finalvalue = 1 × 1 = 1
  - i=2: finalvalue = 1 × 2 = 2
  - i=3: finalvalue = 2 × 3 = 6
  - i=4: finalvalue = 6 × 4 = 24
  - i=5: finalvalue = 24 × 5 = 120
  - Result: 120

### 2. MathModule.py
Demonstrates various mathematical functions from Python's built-in `math` module.

**Features:**
- Square root calculation using `math.sqrt()`
- Natural logarithm using `math.log()`
- Sine calculation using `math.sin()`

**Usage:**
```bash
python MathModule.py
```

**Example:**
```
Enter a number: 10
Square root: 3.162...
Logarithm: 2.302...
Sine: -0.544...
```

**Detailed Explanation:**

This program demonstrates the use of Python's built-in `math` module, which provides access to mathematical functions defined by the C standard.

**Code Breakdown:**
1. **Line 1:** `import math`
   - Imports the math module to access mathematical functions
   - The math module is built-in, so no installation is required
   - This gives access to functions like sqrt, log, sin, cos, tan, etc.

2. **Line 3:** `mathinput = int(input("Enter a number: "))`
   - Prompts the user to enter a number
   - Converts the string input to an integer
   - Stores the value in `mathinput` variable

3. **Line 4:** `print(f"Square root: ", math.sqrt(mathinput))`
   - **`math.sqrt()`** calculates the square root of a number
   - Square root of x is a number that, when multiplied by itself, equals x
   - Example: √10 ≈ 3.162 because 3.162 × 3.162 ≈ 10
   - Returns a float value

4. **Line 5:** `print(f"Logarithm: ", math.log(mathinput))`
   - **`math.log()`** calculates the natural logarithm (base e)
   - Natural logarithm uses Euler's number (e ≈ 2.71828) as the base
   - ln(10) ≈ 2.302 means e^2.302 ≈ 10
   - Useful in exponential growth/decay calculations
   - Returns a float value

5. **Line 6:** `print(f"Sine: ", math.sin(mathinput))`
   - **`math.sin()`** calculates the sine of an angle
   - **Important:** The input is expected in **radians**, not degrees
   - 10 radians ≈ 573 degrees
   - sin(10 radians) ≈ -0.544
   - To convert degrees to radians: `math.radians(degrees)`
   - Returns a value between -1 and 1

**Key Concepts:**
- **math.sqrt(x)**: Returns √x
- **math.log(x)**: Returns ln(x) - natural logarithm (base e)
- **math.sin(x)**: Returns sine where x is in radians

**Common Use Cases:**
- Square root: Distance calculations, geometry
- Logarithm: Data analysis, growth rates, algorithms complexity
- Sine: Physics, engineering, wave calculations

## Requirements
- Python 3.x
- No external libraries required (uses built-in `math` module)
