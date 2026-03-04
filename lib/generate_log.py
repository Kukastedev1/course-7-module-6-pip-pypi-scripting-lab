from datetime import datetime
import os

def generate_log(data):

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # STEP 2: Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write log entries to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)