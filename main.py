from services.storage_service import StorageService
from services.password_service import PasswordService
from controllers.password_controller import PasswordController

storage = StorageService()
password_service = PasswordService()
controller = PasswordController(storage, password_service)

while True:
    print("\n=== Password Manager ===")
    print("1. Add password")
    print("2. Generate password")
    print("3. Show all")
    print("4. Delete")
    print("5. Save & Exit")

    choice = input("> ")

    if choice == "1":
        service = input("Service: ")
        username = input("Username: ")
        password = input("Password: ")
        controller.add_record(service, username, password)

    elif choice == "2":
        length = int(input("Length: "))
        pwd = password_service.generate_password(length)
        print("Generated:", pwd)

    elif choice == "3":
        for i, r in enumerate(controller.list_records()):
            print(i, r)

    elif choice == "4":
        idx = int(input("Index: "))
        controller.delete_record(idx)

    elif choice == "5":
        controller.save()
        break
