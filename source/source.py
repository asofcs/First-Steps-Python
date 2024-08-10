import sklearn 
import typing 
import numpy
import pandas 



def load_dataset(name: typing.Optional[str] = None,)-> numpy.ndarray:
    
    testFlag = False
    dtNew = None
    
    try:
        if (isinstance(name, str) and (name in ['iris','diabetes','digits','wine','linnerud', 'breast_cancer'])):
            
            testFlag = True
        
        else:
            raise Exception

            
    except(Exception, ValueError, TypeError):
        print(f'Invalid dataset - {name} - (load_dataset)')

    if testFlag is True:
        
        match name:
            case 'iris':
                dtNew = sklearn.datasets.load_iris()
            case 'diabetes':
                dtNew = sklearn.datasets.load_diabetes()
            case 'digits':
                dtNew = sklearn.datasets.load_digits()
            case 'wine':
                dtNew = sklearn.datasets.load_wine()
            case 'linnerud':
                dtNew = sklearn.datasets.load_linnerud()
            case 'breast_cancer':
                dtNew = sklearn.datasets.load_breast_cancer()

    del testFlag
    return dtNew


def dataset_info(name: typing.Optional[str] = None,
                 data: typing.Optional[bool] = False,
                 target: typing.Optional[bool] = False,
                 target_names: typing.Optional[bool] = False,
                 feature_names: typing.Optional[bool] = False,
                 filename: typing.Optional[bool] = False, 
                 description: typing.Optional[bool] = False):
    

    
    testFlag = False
    dtNew = None

    try:
        dtNew = load_dataset(name)
        
        if (dtNew is not None):
            
            testFlag = True
        
        else:
            raise Exception

            
    except(Exception, ValueError, TypeError):
        print(f'Invalid dataset - {name} (dataset_info)')
        

    if testFlag is True:
        print('\n\tData Description:\n')

        if ((hasattr(dtNew, 'data')) and (data is True)):
            print('The data matrix:\n', dtNew['data'])

        if ((hasattr(dtNew, 'target')) and (target is True)):
            print('The classification target:\n',dtNew['target'])
        
        if ((hasattr(dtNew, 'feature_names')) and (feature_names is True)):
            print('The names of the dataset columns:\n',dtNew['feature_names'])

        if ((hasattr(dtNew, 'target_names')) and (target_names is True)):
            print('The names of target classes:\n',dtNew['target_names'])

        if ((hasattr(dtNew, 'DESCR')) and (description  is True)):
            print('The full description of the dataset:\n',dtNew['DESCR'])
        
        if ((hasattr(dtNew, 'filename')) and (filename is True)):
            print('The path to the location of the data:\n',dtNew['filename'])
              
    del testFlag
    del dtNew

def dataset2df(name: typing.Optional[str] = None)->pandas.DataFrame:

    testFlag = False
    dtNew = None
    dfNew = None

    try:
        dtNew = load_dataset(name)
        
        if (dtNew is not None):
            
            testFlag = True
        
        else:
            raise Exception

            
    except(Exception, ValueError, TypeError):
        print(f'Invalid dataset - {name} (dataset_info)')
        

    if testFlag is True:
        
        if (hasattr(dtNew, 'data') and hasattr(dtNew, 'target')):

            dataDf = None
            targetDf = None

            
            dataDf = pandas.DataFrame(data = dtNew['data'], 
                                  columns = dtNew['feature_names'])

            targetDf = pandas.DataFrame(data = dtNew['target'])
            targetDf = targetDf.rename(columns = {0: 'target'})

            dfNew  = pandas.concat([dataDf, targetDf], axis = 1)
            dfNew.dropna(how ='any', axis = 0, inplace = True)
           
            print('\n\tFirst values of the data:\n',dfNew.head())

            print('Unique features:\n',dfNew['target'].unique())


            del dataDf
            del targetDf
            
    del testFlag
    del dtNew
    return dfNew  
  
# get description, get scatter for least and most correlated variable with target.
# predict and get confmatrix and scores.
