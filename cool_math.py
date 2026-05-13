#!/usr/bin/env python3
"""
Cool Math Script with Terminal Animations
A visually stunning interactive math calculator with animations and colors
"""

import time
import math
import os
from typing import List, Tuple

# ANSI Color codes
class Colors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title: str, color: str = Colors.CYAN):
    """Print a stylish header"""
    width = 60
    print(f"\n{color}{Colors.BOLD}{'═' * width}")
    print(f"╔{'═' * (width - 2)}╗")
    print(f"║ {title.center(width - 4)} ║")
    print(f"╚{'═' * (width - 2)}╝")
    print(f"{'═' * width}{Colors.RESET}\n")


def animate_text(text: str, delay: float = 0.05, color: str = Colors.CYAN):
    """Animate text appearance"""
    for char in text:
        print(f"{color}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(delay)
    print()


def animate_progress_bar(label: str, duration: float = 2.0, color: str = Colors.GREEN):
    """Show animated progress bar"""
    steps = 40
    print(f"{Colors.BOLD}{label}{Colors.RESET}")
    
    for i in range(steps + 1):
        percentage = (i / steps) * 100
        filled = int((i / steps) * 30)
        bar = f"[{color}{'█' * filled}{Colors.RESET}{'░' * (30 - filled)}] {percentage:.0f}%"
        print(f"\r{bar}", end='', flush=True)
        time.sleep(duration / steps)
    
    print(f"\n{Colors.GREEN}✓ Complete!{Colors.RESET}\n")


def show_result(expression: str, result):
    """Display result with cool animation"""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}Calculating: {Colors.CYAN}{expression}{Colors.RESET}")
    print(f"{Colors.MAGENTA}Processing{Colors.RESET}", end='', flush=True)
    
    for _ in range(3):
        time.sleep(0.3)
        print(f"{Colors.MAGENTA}.{Colors.RESET}", end='', flush=True)
    
    print()
    time.sleep(0.3)
    
    print(f"\n{Colors.BOLD}{Colors.GREEN}RESULT:{Colors.RESET}")
    print(f"{Colors.CYAN}{result}{Colors.RESET}\n")
    time.sleep(0.5)


def basic_math():
    """Basic arithmetic operations"""
    print_header("BASIC ARITHMETIC", Colors.GREEN)
    
    try:
        num1 = float(input(f"{Colors.YELLOW}Enter first number: {Colors.RESET}"))
        num2 = float(input(f"{Colors.YELLOW}Enter second number: {Colors.RESET}"))
        
        print(f"\n{Colors.BOLD}Choose operation:{Colors.RESET}")
        print(f"{Colors.CYAN}1. Addition (+)")
        print(f"2. Subtraction (-)")
        print(f"3. Multiplication (*)")
        print(f"4. Division (/)")
        print(f"5. Power (**)")
        print(f"6. Modulo (%)") 
        print(f"7. Floor Division (//){Colors.RESET}")
        
        choice = input(f"\n{Colors.YELLOW}Choose operation (1-7): {Colors.RESET}")
        
        operations = {
            '1': (f"{num1} + {num2}", num1 + num2),
            '2': (f"{num1} - {num2}", num1 - num2),
            '3': (f"{num1} * {num2}", num1 * num2),
            '4': (f"{num1} / {num2}", num1 / num2 if num2 != 0 else "Error: Division by zero"),
            '5': (f"{num1} ** {num2}", num1 ** num2),
            '6': (f"{num1} % {num2}", num1 % num2 if num2 != 0 else "Error: Modulo by zero"),
            '7': (f"{num1} // {num2}", num1 // num2 if num2 != 0 else "Error: Division by zero"),
        }
        
        if choice in operations:
            expr, result = operations[choice]
            show_result(expr, result)
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.RESET}")
    
    except ValueError:
        print(f"{Colors.RED}Please enter valid numbers!{Colors.RESET}")


def fibonacci():
    """Generate Fibonacci sequence"""
    print_header("FIBONACCI SEQUENCE", Colors.BLUE)
    
    try:
        n = int(input(f"{Colors.YELLOW}How many Fibonacci numbers? {Colors.RESET}"))
        
        if n <= 0:
            print(f"{Colors.RED}Please enter a positive number!{Colors.RESET}")
            return
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        print(f"\n{Colors.YELLOW}Generating {n} Fibonacci numbers...{Colors.RESET}\n")
        time.sleep(0.5)
        
        for i, num in enumerate(fib[:n]):
            print(f"{Colors.BLUE}{i:2d}. {Colors.CYAN}{num:>15,}{Colors.RESET}", end='')
            if (i + 1) % 3 == 0:
                print(f" {Colors.MAGENTA}✨{Colors.RESET}")
            else:
                print()
            time.sleep(0.2)
        
        print()
    
    except ValueError:
        print(f"{Colors.RED}Please enter a valid number!{Colors.RESET}")


def prime_checker():
    """Find prime numbers in a range"""
    print_header("PRIME NUMBER FINDER", Colors.MAGENTA)
    
    try:
        start = int(input(f"{Colors.YELLOW}Start number: {Colors.RESET}"))
        end = int(input(f"{Colors.YELLOW}End number: {Colors.RESET}"))
        
        if start > end:
            print(f"{Colors.RED}Start must be less than or equal to End!{Colors.RESET}")
            return
        
        primes = []
        print(f"\n{Colors.YELLOW}Searching for primes between {start} and {end}...{Colors.RESET}\n")
        
        for num in range(start, end + 1):
            is_prime = num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
            
            if is_prime:
                primes.append(num)
                print(f"{Colors.GREEN}Found: {Colors.CYAN}{num:>3d}{Colors.RESET} ", end='', flush=True)
                time.sleep(0.1)
            else:
                print(f"{Colors.DIM}.{Colors.RESET}", end='', flush=True)
                time.sleep(0.02)
        
        print(f"\n\n{Colors.BOLD}{Colors.GREEN}Total primes found: {len(primes)}{Colors.RESET}\n")
    
    except ValueError:
        print(f"{Colors.RED}Please enter valid numbers!{Colors.RESET}")


def scientific_calc():
    """Scientific calculations"""
    print_header("SCIENTIFIC CALCULATOR", Colors.MAGENTA)
    
    try:
        print(f"{Colors.CYAN}Available operations:")
        print(f"1. Square root (√x)")
        print(f"2. Power (x^y)")
        print(f"3. Factorial (x!)")
        print(f"4. Sine (sin)")
        print(f"5. Cosine (cos)")
        print(f"6. Tangent (tan)")
        print(f"7. Logarithm (log)")
        print(f"8. Natural Log (ln){Colors.RESET}")
        
        choice = input(f"\n{Colors.YELLOW}Choose operation (1-8): {Colors.RESET}")
        
        if choice == '1':
            x = float(input(f"{Colors.YELLOW}Enter number: {Colors.RESET}"))
            result = math.sqrt(x)
            show_result(f"√{x}", result)
        
        elif choice == '2':
            x = float(input(f"{Colors.YELLOW}Base (x): {Colors.RESET}"))
            y = float(input(f"{Colors.YELLOW}Exponent (y): {Colors.RESET}"))
            result = x ** y
            show_result(f"{x}^{y}", result)
        
        elif choice == '3':
            x = int(input(f"{Colors.YELLOW}Enter number: {Colors.RESET}"))
            result = math.factorial(x)
            show_result(f"{x}!", result)
        
        elif choice == '4':
            x = float(input(f"{Colors.YELLOW}Enter angle (degrees): {Colors.RESET}"))
            result = math.sin(math.radians(x))
            show_result(f"sin({x}°)", result)
        
        elif choice == '5':
            x = float(input(f"{Colors.YELLOW}Enter angle (degrees): {Colors.RESET}"))
            result = math.cos(math.radians(x))
            show_result(f"cos({x}°)", result)
        
        elif choice == '6':
            x = float(input(f"{Colors.YELLOW}Enter angle (degrees): {Colors.RESET}"))
            result = math.tan(math.radians(x))
            show_result(f"tan({x}°)", result)
        
        elif choice == '7':
            x = float(input(f"{Colors.YELLOW}Enter number: {Colors.RESET}"))
            result = math.log10(x)
            show_result(f"log₁₀({x})", result)
        
        elif choice == '8':
            x = float(input(f"{Colors.YELLOW}Enter number: {Colors.RESET}"))
            result = math.log(x)
            show_result(f"ln({x})", result)
        
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.RESET}")
    
    except ValueError as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")


def custom_expression():
    """Evaluate custom mathematical expression"""
    print_header("CUSTOM MATH EXPRESSION", Colors.YELLOW)
    
    print(f"{Colors.CYAN}Enter a math expression (e.g., 2**3 + 5*2, sqrt(16), sin(0)))")
    print(f"Supported: +, -, *, /, **, %, //, sqrt, sin, cos, tan, log, exp, etc.{Colors.RESET}\n")
    
    try:
        expr = input(f"{Colors.YELLOW}Enter expression: {Colors.RESET}")
        
        # Create safe namespace for eval
        safe_dict = {
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'factorial': math.factorial,
            'radians': math.radians,
            'degrees': math.degrees,
        }
        
        result = eval(expr, {"__builtins__": {}}, safe_dict)
        show_result(expr, result)
    
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")


def main_menu():
    """Display main menu"""
    while True:
        clear_screen()
        
        print(f"{Colors.BOLD}{Colors.CYAN}")
        print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        🚀 COOL INTERACTIVE MATH CALCULATOR 🚀           ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
        """)
        print(Colors.RESET)
        
        print(f"{Colors.BOLD}{Colors.GREEN}Choose what to calculate:{Colors.RESET}\n")
        print(f"{Colors.CYAN}1. Basic Arithmetic (+, -, *, /, **, %, //)")
        print(f"2. Fibonacci Sequence")
        print(f"3. Prime Number Finder")
        print(f"4. Scientific Calculator")
        print(f"5. Custom Expression")
        print(f"6. Exit{Colors.RESET}\n")
        
        choice = input(f"{Colors.YELLOW}Enter your choice (1-6): {Colors.RESET}")
        
        if choice == '1':
            basic_math()
        elif choice == '2':
            fibonacci()
        elif choice == '3':
            prime_checker()
        elif choice == '4':
            scientific_calc()
        elif choice == '5':
            custom_expression()
        elif choice == '6':
            print(f"\n{Colors.YELLOW}Thanks for using Cool Math! Goodbye!{Colors.RESET}\n")
            break
        else:
            print(f"{Colors.RED}Invalid choice! Please try again.{Colors.RESET}")
            time.sleep(1)
        
        input(f"\n{Colors.BOLD}{Colors.MAGENTA}Press Enter to continue...{Colors.RESET}")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Program interrupted. Goodbye!{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}\n")
