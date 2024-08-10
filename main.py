import source.source as scr
#import sklearn
#import pandas


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
    del df

if __name__ == "__main__":
    main()
