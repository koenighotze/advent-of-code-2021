import sys
import re
from common import load_data
from statistics import median


def part1(lines):
    counts = [0] * 9

    for line in lines:
        [_, out] = re.split(r"\s+\|\s+", line)

        for word in re.split(r"\W+", out):
            if len(word) == 2:
                print(word) 
            counts[len(word)] += 1

    for i in [0, 1, 5, 6]:
        counts[i] = 0
    
    print(counts)

    return { 
        'sum_of_all': sum(counts),
        '1': counts[2],
        '4': counts[4],
        '7': counts[3],
        '8': counts[7]
    }


if __name__ == "__main__":
    RESULT = part1(load_data(sys.argv[1]))
    print(f"Result is: {RESULT['sum_of_all']}")
