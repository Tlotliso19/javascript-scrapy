import os

# Access the secret stored in the environment variable
my_secret = os.getenv('MY_SECRET_KEY')

# Use the secret (e.g., print or make an API call)
print(f"My secret is: {my_secret}")
