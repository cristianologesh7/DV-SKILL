import pickle

files = ["INFO.bin", "ERROR.bin"]

for filename in files:

    try:
        print("\nReading", filename)

        with open(filename, "rb") as file:

            while True:

                try:
                    record = pickle.load(file)

                    print("----------------------------")
                    print("Timestamp :", record["Timestamp"])
                    print("Server    :", record["Server"])
                    print("Level     :", record["Level"])
                    print("Message   :", record["Message"])

                except EOFError:
                    break

    except FileNotFoundError:
        print(filename, "not found")