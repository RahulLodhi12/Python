content=True
i=1
with open("log.txt") as f:
    while content:
        content = f.readline().lower()
        if "python" in content: # case sensitive
            print(content)
            print(f"Yes, Python is present in line no. {i}")
            print(i)
        i+=1