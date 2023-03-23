import sys

# Define counters and variables
status_code_count = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_file_size = 0
line_count = 0

try:
    # Read input line by line
    for line in sys.stdin:
        line_count += 1

        # Split the input line into fields
        fields = line.split(" ")
        status_code = fields[8]
        file_size = fields[9]

        # Update counters
        total_file_size += int(file_size)
        status_code_count[status_code] += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    # Print final metrics on keyboard interruption
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print("{}: {}".format(code, count)))
