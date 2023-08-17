with open("log.txt") as f:
    content = f.read().lower()

if "python" in content: # case sensitive
    print("Yes, Python is present")
else:
    print("No, Python is not present")