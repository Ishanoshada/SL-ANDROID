import re

SYNTAX_RULES = {
    # Print statements
     r'penn\s+"(.+)"': r'print("\1")',  # penn "Hello" → print("Hello")
    r'penn\s+(.+)': r'print(\1)',      # penn x → print(x)
    r'penn\s*\((.*)\)': r'print(\1)',  # penn(x) → print(x)
    
    # For loops
    r'for\s+(\w+)\s+in\s+(\d+)\s+to\s+(\d+):': r'for \1 in range(\2, \3 + 1):',  # for i in 1 to 5: → for i in range(1, 6):

    # Variable assignments
    r'(\w+)\s*=\s*(.+)': r'\1 = \2',  # x = 10 → x = 10

    # Function definitions
    r'func\s+(\w+)\((.*)\):': r'def \1(\2):',  # func add(a, b): → def add(a, b):

    # If-else statements
    r'if\s+(.+):': r'if \1:',          # if x > 10: → if x > 10:
    r'else:': r'else:',                # else: → else:

    # While loops
    r'while\s+(.+):': r'while \1:',    # while x > 0: → while x > 0:

    # Comments (remove them)
    r'#.*': '',                        # # This is a comment → (removed)

    # List literals
    r'\[(.+)\]': r'[\1]',              # [1, 2, 3] → [1, 2, 3]

    # List comprehensions
    r'\[(.+)\s+for\s+(\w+)\s+in\s+(.+)\]': r'[\1 for \2 in \3]',  # [x * 2 for x in nums] → [x * 2 for x in nums]

    # Dictionaries
    r'\{([^:]+):\s*(.+)\}': r'{\1: \2}',  # {"key": value} → {"key": value}

    # String formatting
    r'(\w+)\s*\+\s*"(.+)"': r'\1 + "\2"',  # name + "!" → name + "!"

    # Lambda functions
    r'lambda\s+(\w+):\s*(.+)': r'lambda \1: \2',  # lambda x: x * 2 → lambda x: x * 2

    # Ternary operator
    r'(\w+)\s+if\s+(.+)\s+else\s+(.+)': r'\1 if \2 else \3',  # x if condition else y → x if condition else y

    # Import statements
    r'ganin\s+(\w+)': r'import \1',  # import math → import math

    # Return statements
    r'return\s+(.+)': r'return \1',  # return result → return result
}

def translate_sa_to_python(sa_code):
    """
    Translate SlandroidScript (.sa) code into Python code using the syntax rules dictionary.
    """
    python_code = sa_code

    # Apply each syntax rule
    for pattern, replacement in SYNTAX_RULES.items():
        python_code = re.sub(pattern, replacement, python_code)

    return python_code

def compile_sa_file(sa_file):
    """
    Compile a .sa file into a Python file.
    """
    with open(sa_file, "r") as file:
        sa_code = file.read()

    python_code = translate_sa_to_python(sa_code)

    # Save the translated Python code to a temporary file
    temp_file = sa_file.replace(".sa", "_compiled.py")
    with open(temp_file, "w") as file:
        file.write(python_code)

    return temp_file