import pandas as pd
import typing as tp


def assign_col(name : tp.Optional[str] = None,
               nindex: tp.Optional[int] = None,
               icol: tp.Optional[int] = None,
               values: tp.Optional[dict] = None,)->bool:
    
    """ assign_col: Fill column with index icol
    
    # parameters:
    #   name: name of the dataframe. Type: str. 
    #   nindex: total number of indexes. Type: int.
    #   icol: index of the column to fill. Type: int.
    #   values: dictionary with values to fill. Type: dict. key: column, list of values: values to fill.

    # return: IF success: TRUE. ELSE: FALSE
    """
    
    if ((values is not None) and
        (name is not None) and
        (len(values.keys()) >= icol) and
        (len(values[icol]) == nindex)):

        globals()[f'{name}'][icol] = values[icol]
        
        return True
        
    else:
        
        return False
    

def assign_namevar(name: tp.Optional[str] = None)->None:
    
    """ Create variable (dataframe's name)
    
    # parameters:
    #   name: name of the dataframe. Type: str. 

    # return: - . IF success: Assign name of dataframe.
    """
    
    if (f'{name}' not in globals().keys()):
        
        globals()[f'{name}'] = None

def assign_dim(name : tp.Optional[str] = None,
               nindex : tp.Optional[int] = None,
               ncols : tp.Optional[int] = None,)->pd.DataFrame:

    """ Create dataframe with required dimensions

    # parameters:
    #  name: name of the dataframe. Type: str.
    #  nindex: total number of indexes. Type: int.
    #  ncols: total number of columns. Type: int.

    #return: IF success: Empty dataframe with required dimensions. ELSE: None.
    """

    if (f'{name}' in globals().keys() and
        (ncols > 0) and
        (nindex > 0)):
        
        globals()[f'{name}'] = pd.DataFrame(columns = range(ncols), index = range(nindex))

    return globals().[f'{name}']

def assign_values(name : tp.Optional[str] = None,
                  values : tp.Optional[dict] = None,)->pd.DataFrame:
    
    """ Fill dataframe by columns
    
    # parameters:
    #  name: name of the dataframe. Type: str.
    #  values: dictionary with values to fill. Type: dict. key: column, list of values: values to fill.  

    # return: IF success: Filled dataframe with ncols. ELSE: Empty dataframe or None.
    """
    testCol = False
    
    if((f'{name}' in globals().keys()) and
      (values is not None) and
      (len(values.keys()) > 0 ):
        
        for idCol in range(globals().[f'{name}'].shape[1]):
            
            testCol = assign_col(f'{name}', globals().[f'{name}'].shape[0], idCol, values)

            if testCol is False:
                
                continue
                
    del testCol
    
    return globals().[f'{name}']

