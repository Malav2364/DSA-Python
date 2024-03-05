for i in range(35):
    def decimal_other(value,choice):
        if choice==1:
            return int(str(value),10)
        elif choice==2:
            return bin(value)
        elif choice==3:
            return oct(value)
        elif choice==4:
            return hex(value)
        else:
            return "Invalid options"
    def binary_other(value,choice):
        if choice==1:
            return bin(value)
        elif choice==2:
            return int(str(value),2)
        elif choice==3:
            return oct(value)
        elif choice==4:
            return hex(value)
        else:
            return "Invalid options"
    def octal_other(value,choice):
        if choice==1:
            return oct(value)
        elif choice==2:
            return bin(value)
        elif choice==3:
            return int(str(value),8)
        elif choice==4:
            return hex(value)
        else:
            return "Invalid options"
    def hexa_other(value,choice):
        if choice==1:
            return hex(value)
        elif choice==2:
            return int(str(value),16)
        elif choice==3:
            return oct(value)
        elif choice==4:
            return bin(value)
        else:
            return "Invalid options"
    print("convet from 1.decimal, 2.binary, 3.octal, 4.hexadecimal")
    input_choice=int(input("enter the choice:"))
    if input_choice==1:
        decimal_num=int(input("enter decimal number:"))
        print("convet from 1.decimal, 2.binary, 3.octal, 4.hexadecimal")
        choice = int(input("enter the target conversion:"))
        print("converted value:",decimal_other(decimal_num,choice))
    elif input_choice==2:
        binary_num=int(input("enter binary number:"))
        print("convet from 1.binary, 2.decimal, 3.octal, 4.hexadecimal")
        choice = int(input("enter the target conversion:"))
        print("converted value:",binary_other(binary_num,choice))
    elif input_choice==3:
        octal_num=int(input("enter octal number:"))
        print("convet from 1.octal 2.binary 3.decimal 4.hexadecimal")
        choice = int(input("enter the target conversion:"))
        print("converted value:",octal_other(octal_num,choice))
    elif input_choice==4:
        hex_num=int(input("enter hexa number:"))
        print("convet from 1.hexadecimal, 2.decimal, 3.octal, 4.binary")
        choice = int(input("enter the target conversion:"))
        print("converted value:",hexa_other(hex_num,choice))