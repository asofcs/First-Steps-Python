import source.source as src

def main():
    
    src.assign_namevar('test')

    print(globals()['test'])


if __name__ == "__main__":
    main()
