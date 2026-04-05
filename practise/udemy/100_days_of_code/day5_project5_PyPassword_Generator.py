import string
import random
from common.utility import get_valid_input

uppercase = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']
lowercase = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']
digits = list(string.digits)              # ['0', '1', ..., '9']
symbols = list(string.punctuation)        # ['!', '"', '#', '$', ...]


nr_uppercase = get_valid_input("How many uppercase letters you like in your password? (Minimum: 1 or Maximum: 2)\n",
                               valid_choices=range(1, 3),
                               cast_type=int)

nr_lowercase = get_valid_input("How many lowercase letters you like in your password? (Minimum: 4 or Maximum: 7)\n",
                               valid_choices=range(4, 8),
                               cast_type=int)

nr_symbols = get_valid_input("How many symbols you like in your password? (Minimum: 1 or Maximum: 2)\n",
                               valid_choices=range(1, 3),
                               cast_type=int)

nr_numbers = get_valid_input("How many numbers you like in your password? (Minimum: 1 or Maximum: 3)\n",
                               valid_choices=range(1, 4),
                               cast_type=int)

# Easy Level
password1 = ""
for char in range(nr_uppercase):
    password1 += random.choice(uppercase)

for char in range(nr_lowercase):
    password1 += random.choice(lowercase)

for char in range(nr_symbols):
    password1 += random.choice(digits)

for char in range(nr_numbers):
    password1 += random.choice(symbols)
print("\n-----------------------------------------")
print(f"Your Easy Password is: {password1}")

# Hard Level
password_list = []
for char in range(nr_uppercase):
    password_list.append(random.choice(uppercase))

for char in range(nr_lowercase):
    password_list.append(random.choice(lowercase))

for char in range(nr_symbols):
    password_list.append(random.choice(digits))

for char in range(nr_numbers):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password2 = ""
for char in password_list:
    password2 += char

print(f"Your Hard Password is: {password2}")

# ---------------------------------------------------------------------------

# Approach-2

# Build character pool
password_chars = (
        random.choices(uppercase, k=nr_uppercase)
        + random.choices(lowercase, k=nr_lowercase)
        + random.choices(symbols, k=nr_symbols)
        + random.choices(digits, k=nr_numbers)
)

print("\n-----------------------------------------")
# Easy - characters in order
print(f"Your Easy Password is: {''.join(password_chars)}")

# Hard - shuffled
random.shuffle(password_chars)
print(f"Your Hard Password is: {''.join(password_chars)}")
