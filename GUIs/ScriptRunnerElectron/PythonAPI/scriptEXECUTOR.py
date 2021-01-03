import sys


# Use arguments to execute different functions

# Example function
def helloworld():
    print("hello from python <br>")


if sys.argv[1] == 'hello':
    helloworld()
# End of example function

arguments = []
arguments.append(sys.argv)
print(arguments)
