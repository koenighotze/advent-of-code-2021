import sys

def day1(measures):
    window_size = 3
    window = lambda values, pos: values[pos:pos + window_size]

    number_of_increases = 0
    for i in range(len(measures) - window_size):
        if (sum(window(measures, i + 1)) > sum(window(measures, i))):
            number_of_increases += 1
            
    return number_of_increases

def load_data(file_name):
    file = open(file_name, 'r')
    return list(map(lambda l: int(l.strip()), file.readlines()))

if __name__ == '__main__':
    number_of_increases = day1(load_data(sys.argv[1]))
    print(f"Number of increases {number_of_increases}")
