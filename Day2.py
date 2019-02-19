import sys


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    sum = a + b
    print(sum)

    my_array()


def my_array():
    array = [0, 10, 20, 30]
    print(array[2])


if __name__ == "__main__":
    main()
