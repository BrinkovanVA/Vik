class TestClass:

    def __init__(self):
        self.public_variable = "I'm public!"
        self.__private_variable = "I'm too shy to be public!"

    def get_public_variable(self):
        return self.public_variable

    def get_private_variable(self):
        return self.__private_variable

if __name__ == "__main__":
    test_class = TestClass()
    print(" ".join(["Public variable:", test_class.get_public_variable()]))
    print(" ".join(["Public variable:", test_class.public_variable]))

    print(" ".join(["Private variable:", test_class.get_private_variable()]))
    print(" ".join(["Private variable:", test_class._private_variable]))