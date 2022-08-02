from executive import Executive

def main():

    filename = input("Enter the name of the input file: ")
    my_exec = Executive(filename)
    my_exec.run()

if __name__ == "__main__":
    main()
