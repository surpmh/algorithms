def main():
    A, B, V = map(int, input().split())

    result = (V - B) // (A - B)

    if (V - B) % (A - B) == 0:
        print(result)
    else:
        print(result + 1)

if __name__ == "__main__":
    main()