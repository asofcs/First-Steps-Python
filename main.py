from scripts.model import ModelClassification
# import pandas
# import sklearn

def main():
    new_model = ModelClassification()
    new_model.set_model("iris","GBoost",
                        "MinMax", True,
                        True, False,
                        False, False,
                        False)
    del new_model


if __name__ == "__main__":
    main()
