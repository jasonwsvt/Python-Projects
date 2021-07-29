#Creating a class with three properties, one public, one protected, and one private.

class PriPro():
    public = None
    __private = None
    _protected = None

# Creating an instance of the class.
p = PriPro()

# A series of tries and excepts for the public property.
try: public = p.public
except: print("\nReading the value of p.public failed.")
else: print("\nThe initial value of p.public is '{}'".format(p.public))
try: p.public = "This is a public class property."
except: print("Assigning a value to p.public failed.")
else: print("Assigning a value to p.public was successful.")
try: print("The final value of p.public is '{}'".format(p.public))
except: print("Reading the value of p.public failed.")

# A series of tries and excepts for the protected property.
try: protected = p._protected
except: print("\nReading the value of p._protected failed.")
else: print("\nThe initial value of p._protected is '{}'".format(p._protected))
try: p._protected = "This is a protected class property."
except: print("Assigning a value to p._protected failed.")
else: print("Assigning a value to p._protected was successful.")
try: print("The final value of p._protected is '{}'".format(p._protected))
except: print("Reading the value of p._protected failed.")

# A series of tries and excepts for the private property.
# Interesting setting a variable equal to the property failed,
# but using its value in a print statement was successful.
try: pvt = p.__private
except: print("\nReading the value of p.__private failed.")
else:print("The initial value of p.__private is '{}'".format(p.__private))
try: p.__private = "This is a private class property."
except: print("Assigning a value to p.__private failed.")
else: print("Assigning a value to p.__private was successful.")
try: print("The final value of p.__private is '{}'".format(p.__private))
except: print("Reading the value of p.__private failed.")