def main():
    T = int(input())

    for test_case in range(1, T+1):
        text = input()
        collection = text.maketrans({
        'a' : '',
        'e' : '',
        'i' : '',
        'o' : '',
        'u' : ''
    })

        print("#{0} {1}".format(test_case, text.translate(collection)))

if __name__ == "__main__":
    main()