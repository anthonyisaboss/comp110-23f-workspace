"""things ill be importing."""

def addition(x:int, y:int):
    return x+ y

my_variable: str = "hello"

if __name__ == "__main__":
    print("this should onlly print when importing my functions.")
else:
    print("this is imported")