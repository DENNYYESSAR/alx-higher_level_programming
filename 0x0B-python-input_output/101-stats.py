#!/usr/bin/python3


import sys


def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("Total file size:", total_size)
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print(f"{code}: {count}")


try:
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}
    count = 0

    for line in sys.stdin:
        count += 1
        parts = line.split()
        if len(parts) > 2:
            try:
                size = int(parts[-1])
                code = int(parts[-2])
                if code in status_codes:
                    status_codes[code] += 1
                total_size += size
            except ValueError:
                pass
        if count == 10:
            print_metrics(total_size, status_codes)
            count = 0

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
    raise
