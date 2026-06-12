from datetime import date
from utils import add, subtract

def main():
    print("Name: Nafiz Noyon")
    print("Today date:", date.today())

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))

if __name__ == "__main__":
    main()
