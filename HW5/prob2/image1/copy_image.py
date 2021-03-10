file = open("image2.jpg", "wb")
with open("image1.jpg", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        file.write(byte[0])
