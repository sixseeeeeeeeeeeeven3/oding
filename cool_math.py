#!/usr/bin/env python3
"""
Cool Math Script with Terminal Animations
A visually stunning math demonstration with animations and colors
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


def fibonacci_animation(n: int = 10):
    """Display Fibonacci sequence with animation"""
    print_header("FIBONACCI SEQUENCE", Colors.BLUE)
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print(f"{Colors.YELLOW}Calculating {n} Fibonacci numbers...{Colors.RESET}\n")
    time.sleep(0.5)
    
    for i, num in enumerate(fib[:n]):
        print(f"{Colors.BLUE}{i:2d}. {Colors.CYAN}{num:>15,}{Colors.RESET}", end='')
        if (i + 1) % 3 == 0:
            print(f" {Colors.MAGENTA}✨{Colors.RESET}")
        else:
            print()
        time.sleep(0.3)
    
    print()


def prime_checker_animation(start: int = 1, end: int = 50):
    """Find and display prime numbers with animation"""
    print_header("PRIME NUMBER FINDER", Colors.MAGENTA)
    
    primes = []
    print(f"{Colors.YELLOW}Searching for primes between {start} and {end}...{Colors.RESET}\n")
    
    for num in range(start, end + 1):
        is_prime = num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
        
        if is_prime:
            primes.append(num)
            print(f"{Colors.GREEN}Found: {Colors.CYAN}{num:>3d}{Colors.RESET} ", end='', flush=True)
            time.sleep(0.1)
        else:
            print(f"{Colors.DIM}.{Colors.RESET}", end='', flush=True)
            time.sleep(0.05)
    
    print(f"\n\n{Colors.BOLD}{Colors.GREEN}Total primes found: {len(primes)}{Colors.RESET}\n")


def matrix_rain_math():
    """Display mathematical operations in matrix style"""
    print_header("MATHEMATICAL OPERATIONS", Colors.GREEN)
    
    operations = [
        ("2² + 3³ =", 2**2 + 3**3),
        ("√144 =", math.sqrt(144)),
        ("sin(π/2) =", math.sin(math.pi/2)),
        ("cos(0) =", math.cos(0)),
        ("log₁₀(1000) =", math.log10(1000)),
        ("e^2 ≈", math.exp(2)),
        ("π² ≈", math.pi**2),
    ]
    
    for operation, result in operations:
        print(f"{Colors.MAGENTA}{operation:<20}{Colors.YELLOW}", end='', flush=True)
        animate_text(f"{result:.6f}", delay=0.02, color=Colors.CYAN)
        time.sleep(0.3)
    
    print()


def fractal_tree(n: int = 3):
    """Display a cool fractal tree visualization"""
    print_header("FRACTAL TREE (Binary Math)", Colors.RED)
    
    def draw_tree(depth: int, width: int = 30, indent: int = 0):
        if depth == 0:
            return
        
        spaces = " " * (30 - width // 2)
        branch = "█" * width
        
        color = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN][depth % 4]
        print(f"{spaces}{color}{branch}{Colors.RESET}")
        time.sleep(0.3)
        
        draw_tree(depth - 1, width // 2 + 1, indent)
        draw_tree(depth - 1, width // 2 + 1, indent)
    
    draw_tree(n)
    print()


def spinning_loader(duration: float = 2.0):
    """Display spinning loader animation"""
    spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for spinner in spinners:
            print(f"\r{Colors.CYAN}{spinner} Processing calculations...{Colors.RESET}", end='', flush=True)
            time.sleep(0.1)
    
    print(f"\r{Colors.GREEN}✓ Done!{Colors.RESET}          \n")


def numerical_sequences():
    """Display cool numerical patterns"""
    print_header("NUMERICAL PATTERNS", Colors.YELLOW)
    
    # Pascal's Triangle
    print(f"{Colors.BOLD}Pascal's Triangle:{Colors.RESET}\n")
    for i in range(7):
        print(" " * (7 - i), end='')
        for j in range(i + 1):
            val = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            print(f"{Colors.MAGENTA}{val:>4}{Colors.RESET}", end=' ')
            time.sleep(0.1)
        print()
    
    print()


def main():
    """Main function to run all demonstrations"""
    clear_screen()
    
    print(f"{Colors.BOLD}{Colors.CYAN}")
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        🚀 COOL MATH WITH AWESOME ANIMATIONS 🚀          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    print(Colors.RESET)
    
    time.sleep(1)
    
    # Run all demonstrations
    animate_progress_bar("Starting math show...", 1.5, Colors.CYAN)
    
    fibonacci_animation(12)
    time.sleep(0.5)
    
    prime_checker_animation(1, 60)
    time.sleep(0.5)
    
    matrix_rain_math()
    time.sleep(0.5)
    
    spinning_loader(2.0)
    
    numerical_sequences()
    time.sleep(0.5)
    
    fractal_tree(3)
    time.sleep(0.5)
    
    # Final message
    print_header("🎉 SHOW COMPLETE! 🎉", Colors.GREEN)
    animate_text("Thanks for watching the cool math animations!", delay=0.03, color=Colors.CYAN)
    print(f"\n{Colors.BOLD}{Colors.YELLOW}Run this script again to see more!{Colors.RESET}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Program interrupted. Goodbye!{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}\n")
