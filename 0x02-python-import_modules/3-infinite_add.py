#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    result = 0
    for i in sys.argv[1:]:
        try:
            result = 0
        except ValueError:
        print(f"Skipping non-integer argument: {i}")

        print("{}".format(result))
