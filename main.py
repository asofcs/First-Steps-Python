from scripts.model import ModelClassification

def main():
    new_model = ModelClassification()
    new_model.set_model("iris","GBoost",
                        "MinMax", True,
                        False, False,
                        False, False,
                        False)
    del new_model


if __name__ == "__main__":
    main()