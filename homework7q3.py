
def main():
    height = float(input("Enter the initial height in meters: "))
    bounces = 0

    while height >= 0.001:
        height = height * 0.60
        bounces = bounces + 1

    print("Number of bounces:", bounces)


main()
