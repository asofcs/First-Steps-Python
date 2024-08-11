import source.source as scr
#import sklearn.datasets 
#import pandas
#import matplotlib.pyplot

def main():
  
    df = None
    scr.dataset_info('iris',
                     True,
                     True,
                     True,
                     True,
                     True,
                     True)

    df = scr.dataset2df('iris')
    scr.dataset_analysis(df)
    del df

if __name__ == "__main__":
    main()
