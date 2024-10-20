from functools import wraps
    
def input_error(func):
    """
    Декоратор для обробки помилок введення користувача. 
    Обробляє KeyError, ValueError, IndexError. 
    """
    @wraps (func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: You must provide both a name and phone."
        except IndexError:
            return "Error: Not enough arguments provided." 
    return inner

def parse_input(user_input):
    """ 
    Розбиває вхідний рядок на команду і аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    """ 
    Додає новий контакт до словника.
    """
    if len(args) < 2:
        raise ValueError 
    name, phone = args[0].title(), args[1]  
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(args, contacts):
    """
    Змінює телефон існуючого контакту.
    """
    if len(args) < 2:
        raise ValueError 
    name, new_phone = args[0].title(), args[1]
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated with new phone number {new_phone}."
    else:
        raise KeyError
    
@input_error
def show_phone(args, contacts):
    """ 
    Відображає телефон контакту.
    """
    if len(args) < 1:
        raise IndexError   
    name = args[0].title() 
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError
 
@input_error    
def show_all(contacts):   
    """ 
    Відображає всі контакти.
    """
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found." 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
    
    
    

    
    """
    1. Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
    2. Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
    3. Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
    4. Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.
    
    """
