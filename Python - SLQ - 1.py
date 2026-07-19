username = input("Please enter your username. ")
print("Welcome, " + username + "!")

size_mb = float(input("Please enter the file size in Megabytes (MB). "))

size_bytes = (size_mb) * (2**20)
print("The size of the file in bytes = " , size_bytes)

print("The exact number of memory blocks required = " , (size_bytes / 4096))

print("The number of completely full memory blocks the file will occupy = " , int(size_bytes // 4096))

print("The exact number of leftover bytes that do not perfectly fit into a full block = " , ((size_bytes / 4096) - (size_bytes // 4096)) * (4096))




