def add(*args):  # unlimited positional arguments: these get passed into the function as a tuple
    return sum(args)


def calculate(n, **kwargs):  # unlimited keyword arguments: these get passed in as a dictionary
    print(kwargs)

    # note that if either add= or multiply= have no values, we will get an error HOWEVER LOOK AT LINE 17
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car:  # you can use kwargs to initialize a class, too
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")  # if .get is used instead it can return "None", a valid value
