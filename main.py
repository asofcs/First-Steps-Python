#import pandas
import functions.functions as fcts

def main():
    
    fcts.assign_namevar('test')
    
    globals()['test'] = fcts.assign_dim('test', 1, 1)
    
    globals()['test'] = fcts.assign_values('test', {0: [3], 1: [5]})
    
    print(globals()['test'])


if __name__ == "__main__":
    main()

