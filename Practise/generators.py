def read_large_log_file(file_path):
    """A generator that reads a huge log file line by line."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # yield each line instead of returning all at once

# Using the generator
for log_line in read_large_log_file("server_logs.txt"):
    if "ERROR" in log_line:
        print("Found error:", log_line)
