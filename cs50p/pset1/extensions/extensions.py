# Ask for file name
x = input("File name: ").strip().lower()

# If the greeting ends with .gif
if x.endswith(".gif") == True:
    print("image/gif")

# If the greeting ends with .jpg
elif x.endswith(".jpg") == True or x.endswith(".jpeg") == True:
    print("image/jpeg")

# If the greeting ends with .png
elif x.endswith(".png") == True:
    print("image/png")

# If the greeting ends with .pdf
elif x.endswith(".pdf") == True:
    print("application/pdf")

# If the greeting ends with .txt
elif x.endswith(".txt") == True:
    print("text/plain")

# If the greeting ends with .zip
elif x.endswith(".zip") == True:
    print("application/zip")

# For all other cases
else:
    print("application/octet-stream")