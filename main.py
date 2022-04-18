import ReflectionMatrix

if __name__ == "__main__":

    InitGuide = "Select Calculation Model\n" \
                "1--ReflectionMatrix"
    print(InitGuide)
    SelectMode = input("MODEL:")
    if SelectMode == "1":
        print("Selected Calculation Model 1--ReflectionMatrix")
        ReflectionMatrix.calculate_ref()
    else:
        print("Require Legal Parameters")
