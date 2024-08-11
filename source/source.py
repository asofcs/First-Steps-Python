import sklearn.datasets 
import typing 
import numpy
import pandas 
import matplotlib.pyplot



def heat_map(xLegend: typing.Optional[list] = None, yLegend: typing.Optional[list] = None,
             sTitle: typing.Optional[str] = None, valMatrix: typing.Optional[numpy.ndarray] = None):
     
    """ Plot a heat map
    
    # parameters:
    #  xLegend: legend of axis x. Type: list.
    #  yLegend: legend of axis y. Type: list.
    #  sTitle: Title. Type: str.
    #  valMatrix: Matrix with values to plot. Type: numpy.ndarray


    # return: - 
    # LINK: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
    """
        
    fig, ax = matplotlib.pyplot.subplots()
    im = ax.imshow(valMatrix)

        
    # Show all ticks and label them with the respective list entries
    ax.set_xticks(numpy.arange(len(xLegend)), labels = xLegend)
    ax.set_yticks(numpy.arange(len(yLegend)), labels = yLegend)
        
    # Rotate the tick labels and set their alignment.
    matplotlib.pyplot.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(yLegend)):
        for j in range(len(xLegend)):
            text = ax.text(j, i, round(valMatrix[i, j], 2), ha="center", va="center", color="w")


    ax.set_title(sTitle)
    fig.tight_layout()
    matplotlib.pyplot.show()
    

    


def create_map_dict (origList: typing.Optional[list] = None,
                     finalList: typing.Optional[list] = None,)->dict:
    
    """ Create dictionary from two lists, to map a dataframe.
    
    # parameters:
    #  origList: list of the original values (keys).
    #  finalList: list of the final values (values).

    # return: IF success: filled dictionary. ELSE: empty dictionary
    """
    
    dMap = None
    
    if((origList is not None) and (finalList is not None)):
        
        if (len(origList) == len(finalList)):

            dMap = {elem : finalList[idVal] for idVal, elem in enumerate(sorted(origList))}

    return dMap

def inv_map(origMap: typing.Optional[dict] = None,)->dict: 

    
    """ Reverse a dictionary to map a dataframe.
    
    # parameters:
    #  origMap: original dictionary. Type: dict

    # return: IF success: reversed dictionary. ELSE: empty dictionary.
    """
    
    invMap = dict()
    testFlag = False 
    
    try:
        
        if((origMap is not None) and (isinstance(origMap, dict)) and (origMap.keys())):
            
            testFlag = True
        else:
            raise Exception

            
    except(Exception, ValueError, TypeError):
        print(f'Invalid dictionary - (inv_map)')
        
    if (testFlag is True):
        
        invMap = {origMap[idKey]: idKey for idKey in origMap.keys()}

    del testFlag

    return invMap

                

def load_dataset(name: typing.Optional[str] = None,)-> sklearn.utils.Bunch:
    
    """ Load dataset from the sklearn.datasets package 
    
    # parameters:
    #  name: name of dataset to import. Type: str.

    # return: IF success: dataset (data, target, target_names, feature_names, filename, description). ELSE: None
    """
    
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
    
    """ Print attribute from dataset if flag is True.
    
    # parameters:
    #  name: name of dataset. Type: str.
    #  data: data flag. Type: bool.
    #  target: target flag. Type: bool.
    #  target_names: target_names flag. Type: bool.
    #  feature_names: feature_names flag. Type: bool.
    #  filename: filename flag. Type: bool.
    #  description: description flag. Type: bool.

    # return: -
    """
    
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
        print('\n\tDATA DESCRIPTION:\n')

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

def dataset2df(name: typing.Optional[str] = None)->dict:

    """ data and target from dataset to dataframe (Alternative to - load_X(as_frame = True))
    
    # parameters:
    #  name: name of dataset. Type: str.
 
    # return: IF success: dictionary with dataframe and dictionary (key: old values of target, values: new values of target). 
    #         ELSE: empty dictionary
    """
    
    testFlag = False
    dtNew = None
    dfNew = None
    dMap = None
    dFinal = dict()

    try:
        dtNew = load_dataset(name)
        
        if (dtNew is not None):
            
            testFlag = True
        
        else:
            raise Exception

            
    except(Exception, ValueError, TypeError):
        print(f'Invalid dataset - {name} (dataset2df)')
        

    if testFlag is True:
        
        print('\n\tDATA CLEANING:\n')

        
        if (hasattr(dtNew, 'data') and hasattr(dtNew, 'target')):

            dataDf = None
            targetDf = None

            
            dataDf = pandas.DataFrame(data = dtNew['data'], 
                                  columns = dtNew['feature_names'])

            targetDf = pandas.DataFrame(data = dtNew['target'])
            targetDf = targetDf.rename(columns = {0: 'target'})

            dfNew  = pandas.concat([dataDf, targetDf], axis = 1)
            dfNew.dropna(how ='any', axis = 0, inplace = True)

            dMap = create_map_dict(dfNew['target'].unique(), dtNew['target_names'])
            dfNew.replace({"target": dMap}, inplace=True)

            dFinal['df'] = dfNew
            dFinal['map'] = dMap
   
            print('First values of the data:\n',dfNew.head())
            print('Unique features:\n',dfNew['target'].unique())

            del dataDf
            del targetDf
            
    del testFlag
    del dtNew
    del dMap
    return dFinal

def dataset_analysis(dFinal: typing.Optional[dict] = None):
    
    """ Print the analysis of the dataset (heat map and statistics)
    
    # parameters:
    #  dFinal: dictionary with dataframe and dictionary (key: old values of target, values: new values of target).

    # return: -
    """
    
    testFlag = False
    invMap = dict()
    auxDf = None
    valMatrix = None

    try:
        
        if (dFinal is not None) and (all(idKey in ['df','map'] for idKey in dFinal.keys())):
            
            testFlag = True
        
        else: 
            
            raise Exception
            
    except(Exception, ValueError, TypeError):
        
        print(f'Invalid dictionary - {name} (dataset_analysis)')

    if testFlag is True:
        
        print('\n\tDATA ANALISYS:\n')

        print('HEAT MAP:\n')

        invMap = inv_map(dFinal['map'])
        auxDf = dFinal['df'].replace({"target": invMap}, inplace = False)
        
        valMatrix = numpy.array(auxDf.corr().to_numpy())

        heat_map(auxDf.columns.tolist(), auxDf.columns.tolist(), "Heat Map", valMatrix)

        print('DATA STATISTICS:\n')
        print(auxDf.describe())

    del valMatrix
    del testFlag
    del invMap
    del auxDf
