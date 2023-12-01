import os
import re


def main():
    calibration = 0
    with open("day_1/puzzle1_input.txt") as file:
        for line in file:
            first_pos = re.search(r"\d", line)
            reverse = line[::-1]
            last_post = re.search(r"\d", reverse)
            calibration += int(line[first_pos.start()]+reverse[last_post.start()])

    print("Calibration: ", calibration)


if __name__ == "__main__":
    main()
