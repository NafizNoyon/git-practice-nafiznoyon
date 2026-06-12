from datetime import date
from utils import add, subtract, multiply, divide

def main():
    print("Name: Nafiz Noyon")
    print("Today date:", date.today())

    try:
        print("Addition:", add(10, 5))
        print("Subtraction:", subtract(10, 5))
        print("Multiplication:", multiply(10, 5))
        print("Division:", divide(10, 0))
    except Exception as error:
        print("An error occurred:", error)

if __name__ == "__main__":
    main()