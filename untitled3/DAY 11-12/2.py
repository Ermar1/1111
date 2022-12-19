file_read = 'config_sw1.txt'
with open(file_read) as file:
    for line in file:
        if '!' in line[0:]:
            continue
        else:
            print(line.strip('\n'))