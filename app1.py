import app2
def print_app1():
    name = (__name__)
    return name

if __name__ == "__main__":
    #The following is calling code from within this script
    print("I am running code from {}".format(print_app1()))

    #The following is calling code from the imported app2.py
    print("I am running code from {}".format(app2.print_app2()));

#I am running code from __main__
#I am running code from app2
