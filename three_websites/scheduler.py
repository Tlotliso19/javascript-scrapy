import schedule
import time
import subprocess
import os


# Path to your Scrapy project root (where scrapy.cfg is located)
root = r'C:\Users\tlotliso.makoboshane\projects\javascript-scrapy\three_websites'

# Path to the .txt file containing the commands
command_file = r'C:\Users\tlotliso.makoboshane\projects\javascript-scrapy\three_websites\scrapy_commands.txt'


import subprocess
import schedule
import time

def run_spider():
    try:


        # Open the command file and read lines
        with open(command_file, 'r', encoding='utf-8-sig') as file:
            commands = [line.strip() for line in file.readlines()]  # Strip newlines and extra spaces

        # Debug print: Show the content of the commands list
        print(f"Commands read from file: {commands}")

        if len(commands) < 2:
            raise ValueError("The command file must contain at least two lines: one for activating the environment, and one for running Scrapy.")

        # Combining the two commands into one
        activate_env_command = commands[0]  # e.g., `call C:\path\to\your\venv\Scripts\activate`
        scrapy_command = commands[1]  # e.g., `scrapy crawl my_spider`

        # The full command that activates the environment and runs Scrapy
        full_command = f"cmd /c {activate_env_command} && {scrapy_command}"

        # Debug print: Show the full command
        print(f"Full command to run: {full_command}")

        # Run the combined command using subprocess
        result = subprocess.run(full_command, cwd=root, check=True, capture_output=True, text=True, shell=True)

        # Output the result
        print(f"Spider ran successfully: {result.stdout}")

    except subprocess.CalledProcessError as e:
        print(f"Error running spider: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Schedule the spider to run every day at 17:17 (5:17 PM)
schedule.every().day.at("00:02").do(run_spider)

# Keep the script running to allow the scheduling to happen
while True:
    schedule.run_pending()  # Run the pending scheduled tasks
    time.sleep(60)  # Wait for one minute before checking again
