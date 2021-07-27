import random, math

## generates main menu options
def main():
    print(33*"=")
    print("MAIN MENU")
    print(33*"=", "\n")
    print(5*" ", "1 - Generate Secure Password.\n")
    print(5*" ", "2 - Calculate and Format a Percentage.\n")
    print(5*" ", "3 - How many days from today until July 4, 2025?\n")
    print(5*" ", "4 - Use the Law of Cosines to calculate the leg of a triangle.\n")
    print(5*" ", "5 - Calculate the volume of a Right Circular Cylinder.\n")
    print(5*" ", "q - Exit program.\n")
    print(33*"=", "\n")

## quick decision options
## reduces redundant code
def quick_menu():
    print("Would you like to return to the Main Menu?")
    quick_input = str(input("Enter 'YES' to continue or 'Q' to quit: "))
    if quick_input.upper() == "YES":
        print("\n")
        menu_select()
    elif quick_input.upper() == "Q":
        print("\nExiting...")
        print("Thank you for using my application!")
        raise SystemExit
    else:
        print("\n!!!!!NOT A VALID INPUT!!!!!")
        print("<<<Enter a valid input.>>>\n")
        quick_input = str(input("Enter 'YES' to continue or 'Q' to quit: "))
       
## main menu CLI
def menu_select():
    main()
    user_input = 0
    user_input = str(input("Input a choice and press enter: "))
    ## continue until 'q' is entered
    while user_input.upper() != "Q":        
        if user_input == "1":
            password_generator()
            break
        elif user_input == "2":
            format_percentage()
            break
        elif user_input == "3":
            date_difference()
            break
        elif user_input == "4":
            law_cosine()
            break
        elif user_input == "5":
            volume_cyliner()
            break
        else:
            print("\n!!!!!NOT A VALID INPUT!!!!!")
            print("<<<Enter a valid input.>>>\n")
            menu_select()
            break
    print("\nExiting...")
    print("Thank you for using my application!")
    raise SystemExit

## password menu + CLI
def password_generator():
    pass_weak = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pass_average = pass_weak + "0123456789"
    pass_strong = pass_weak + pass_average + "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    print("\n")
    print(33*"=")
    print("PASSWORD GENERATOR")
    print(33*"=", "\n")
    print("I need more information about your password.\n")
    password_length = int(input("How long does the password have to be? Use digits: "))
    while password_length != int in range(100):
        print("\n!!!!!NOT A VALID INPUT!!!!!")
        print("<<<Enter a valid input.>>>\n")
        password_length = int(input("How long does the password have to be? Use digits: "))
        break
    print("")
    print(5*" ", "Format 1 - Upper + Lower case letters.\n")
    print(5*" ", "Format 2 - Upper + Lower case + Numbers.\n")
    print(5*" ", "Format 3 - Upper + Lower case + Numbers + Symbols.\n")
    password_format = str(input("Which format *NUMBER* [shown above] should it be? "))
    password_randoms = ""
    if password_format == "1":
        password_randoms += pass_weak
    elif password_format == "2":
        password_randoms += pass_average
    elif password_format == "3":
        password_randoms += pass_strong
    else:
        print("\n!!!!!NOT A VALID INPUT!!!!!")
        print("<<<Enter a numeric input.>>>\n")
        password_format = str(input("Which format *NUMBER* [shown above] should it be? "))
    password = "".join(random.sample(password_randoms, password_length))
    print("Here is your new password:", password)
    print(33*"=", "\n")
    quick_menu()

## calculate and format percentage CLI
def format_percentage():    
    print("\n")
    print(33*"*")
    print("CALCULATE AND FORMAT A PERCENTAGE")
    print(33*"*", "\n")
    print("\nNumerator(a) and Denominator(b) follow a/b, or 'a' divided by 'b' design.\n")
    numerator_input = str(input("Please enter your numerator (a): "))
    ## error free input checks
    if numerator_input.isdigit():
        pass
    else:
        print("\n!!!!!NOT A VALID INPUT!!!!!")
        print("<<<Enter a numeric input.>>>\n")
        numerator_input = str(input("Please enter your numerator (a): "))
    denominator_input = str(input("Please enter your denominator (b): "))
    ## error free input checks
    if denominator_input.isdigit():
        pass
    else:
        print("\n!!!!!NOT A VALID INPUT!!!!!")
        print("<<<Enter a numeric input.>>>\n")
        numerator_input = str(input("Please enter your numerator (a): "))
    ## converts input to floats for calculation
    a = float(numerator_input)
    b = float(denominator_input)
    x = (a/b)*100
    format_input = str(input("How many decimal values do you need? [Digits right of decimal]: "))
    ## error free input checks
    if format_input.isdigit():
        pass
    else:
        print("\n!!!!!NOT A VALID INPUT!!!!!")
        print("<<<Enter a numeric input.>>>\n")
        format_input = str(input("How many decimal values do you need? [Number of digits to right of decimal]: "))
    ## easy creation of required format
    d = "%."+format_input+"f"
    ## converts inputs to the specified format
    decimal_place = d % x +'%'
    print("\nYour percent value computed to", format_input, "decimals is:", decimal_place)
    print("\n")
    print(33*"*","\n")
    quick_menu()

## calculate days to July 4, 2025 CLI
def date_difference():
    from datetime import date
    today = date.today()
    other_date = date(2025, 7, 4)
    num_difference = other_date - today
    print("\n")
    print(33*"*")
    print("COUNTDOWN TO JULY 4, 2025")
    print(33*"*", "\n")
    print("There are",num_difference.days, "days until July 4, 2025.\n")
    print("Assuming no nuclear fallout, alien invasion, or cataclysmic armageddon...\n")
    print(33*"*","\n")
    quick_menu()

## find last leg of a triangle
def law_cosine():
    print("\n")
    print(33*"*")
    print("Cosine Says: c2=a2+b2 −2ab cos(C)")
    print(33*"*", "\n")
    print("To find the lost leg measurement I need some information.\n")
    a = float(input("First known side length is? "))
    b = float(input("Second known side length is? "))
    ang = float(input("The known angle measurement [number value]: "))
    ang_cos = math.cos(ang * 180)
    cosine = (a**2 + b**2 - 2 * a * b * ang_cos)
    cosine_squared = (math.sqrt(cosine))
    ## round answer to 3 decimals
    cosine_answer = str(round(cosine_squared, 3))
    print("The last leg of the triangle is measured:",cosine_answer,'\n')
    print(33*"*","\n")
    quick_menu()

## find volume of a right circular cylinder
def volume_cyliner():
    print("\n")
    print(33*"*")
    print("Volume of Right Circular Cylinder")
    print(33*"*", "\n")
    print("To find the volume I need some information.\n")
    r = float(input("What is the cylinder radius? "))
    h = float(input("What is the cylinder height? "))
    p = math.pi
    V = (p*r**2)*h
    v = str(round(V, 3))
    print("The volume of the cylinder is measured:",v,'\n')
    print(33*"*","\n")
    quick_menu()
        
if __name__ == '__main__':
    menu_select()
