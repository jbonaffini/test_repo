
# password checker

def password_checker() :
    correct_password = "python_pw"
    password = input("Please Enter Password: ")
    while correct_password != password :
        password = input("Wrong Password! Please Enter again: ")
    print("Logged in!")

# temperature practice with files

def temperature_test() :
    temperatures = [10, -20, -289, 100]

    def writer(temperatures, file):
        with open(file, "w") as myfile :
            for c in temperatures :
                if c > -273.15 :
                    f = c* 9/5 + 32
                    myfile.write(str(f) + "\n")

    writer(temperatures, r"basics\temperature_ex.txt")

def filemerge_test() :
    from datetime import datetime
    import glob2

    filenames = glob2.glob("*.txt")
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"

    with open(filename,"w") as curfile :
        for file in filenames :
            with open(file,"r") as f :
                curfile.write(f.read()+'\n')


# control block

# password_checker()
# temperature_test()
filemerge_test()
