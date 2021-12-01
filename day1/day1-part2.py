file1 = open('input', 'r')
Lines = list(map(lambda l: int(l.strip()), file1.readlines()))
windowSize = 3

window = lambda values, pos: values[pos:pos + windowSize]
finished = lambda i: i + windowSize + 1 > len(Lines)

numberOfIncreases = 0
index = 0
while index < len(Lines):
    if (finished(index)):
        break

    if (sum(window(Lines, index + 1)) > sum(window(Lines, index))):
        numberOfIncreases += 1
    index += 1

print(f"Number of increases {numberOfIncreases}")