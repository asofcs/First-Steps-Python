from source.source import PdDataframe

def main():
    
    newdf = PdDataframe()
    newdf.fill_df("test",1,1,{0: [3], 1: [5]})
    print(newdf.df)
    newdf.__del__()


if __name__ == "__main__":
    main()
