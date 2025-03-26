from neural_nets import rectified_linear_unit, rectified_linear_unit_derivative 

def relu_tests():
    print("Running relu_tests")
    if rectified_linear_unit(1) != 1:
        print("Fail, should have returned 1")
    if rectified_linear_unit(-1) != 0:
        print("Fail, should have returned 0")

    if rectified_linear_unit_derivative(100) != 1:
        print("Fail, should have returned 1")

    if rectified_linear_unit_derivative(-100) != 0:
        print("Fail, should have returned 0")

    print("Pass")


if __name__ == "__main__":
    relu_tests()
