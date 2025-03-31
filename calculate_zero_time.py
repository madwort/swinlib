
from swinlib.time import calculate_zero_time

def main():
    # Some observed timestamps from my local db
    calculate_zero_time("2018-12-11 16:37", 566239055.0)
    calculate_zero_time("2025-02-05 21:37", 760484229.379076)
    calculate_zero_time("2025-03-02 10:03", 762602534.625131)


if __name__ == "__main__":
    main()
