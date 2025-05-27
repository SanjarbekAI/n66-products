from core.table_queries import initializing_tables
from utils.crud import add_product, show_products, delete_product


def main():
    print("""
    1. Add product
    1. Add product
    1. Add product
    1. Add product
    1. Add product
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        delete_product()
    else:
        print("Invalid choice")
    return main()


if __name__ == '__main__':
    initializing_tables()
    main()
