with open("C:\\Users\\ks121mitin\\Desktop\\n\\11-12\\config_sw1.txt", 'r') as f:
    for line in f:
        if not line.startswith("!"):
            print(line.rstrip())