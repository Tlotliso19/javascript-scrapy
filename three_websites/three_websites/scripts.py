import os

# Access the secret stored in the environment variable
my_secret = os.getenv('DATABASE_URL')

# Use the secret (e.g., print or make an API call)
print(f"My secret is: {my_secret}")
