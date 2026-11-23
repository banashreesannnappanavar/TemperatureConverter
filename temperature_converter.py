def c_to_f(celsius):
    return (celsius * 9/5) + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


def c_to_k(celsius):
    return celsius + 273.15


def main():
    print("===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter your choice: ")

    if choice == "1":
        celsius = float(input("Enter Celsius: "))
        print("Fahrenheit:", c_to_f(celsius))

    elif choice == "2":
        fahrenheit = float(input("Enter Fahrenheit: "))
        print("Celsius:", f_to_c(fahrenheit))

    elif choice == "3":
        celsius = float(input("Enter Celsius: "))
        print("Kelvin:", c_to_k(celsius))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()