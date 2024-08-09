import typing as tp
import pandas as pd

def check_instance(var : tp.Any , xtype : tp.Any, verror : tp.Any)->tp.Any:
    
    """ Check instance/type of a variable
    
    # parameters:
    #  var: variable to check
    #  xtype: type expected
    #  verror: error value

    # return: IF success: var. ELSE: verror
    """
    
    try:
        
        if (isinstance(var, xtype) is True):
            return var
            
        else:
            raise Exception
            
    except (Exception, ValueError, TypeError):
        return verror



class PdDataframe:
    
    """ DataFrame
    
    # attributes:
    #  name: name of the dataframe
    #  ncols: total number of columns
    #  nindex: total number of indexes
    #  values: dictionary with values to fill
    #  df: dataframe

    # methods:
    #  __init__: constructor.
    #  __add_attributes: update attributes (private).
    #  __assign_dim: create empty dataframe with required dimensions - nindex and ncols (private).
    #  __assign_col: fill column with index icol (private).
    #  __assign_values: fill dataframe by columns (private).
    #  fill_df: includes __add_attributes, __assign_dim, __assign_values (public).
    #  __del__: destructor.


    # return: -
    """
    def  __init__(self):
        
        self.name = None
        self.ncols = 0
        self.nindex = 0
        self.values = None
        self.df = None


    def __add__attributes(self,
                          name,
                          ncols,
                          nindex,
                          values):
        
        """  __add__attributes: update attributes.
        
        # parameters:
        #   self: class. 
        #   name: name of the dataframe. Type: str. 
        #   ncols: total number of columns. Type: int.
        #   nindex: total number of indexes. Type: int.
        #   values: dictionary with values to fill. Type: dict. key: column, list of values: values to fill.
    
        # return: IF success: Update attributes. ELSE: -
        """
        
        self.name =  check_instance(name ,str, None)
        self.ncols = check_instance(ncols, int, 0)
        self.nindex = check_instance(nindex, int, 0)
        self.values = check_instance(values, dict, None)
        self.df =  check_instance(pd.DataFrame(data = None), pd.DataFrame, None)
        
    
    def __assign_dim(self):

        """ __assign_dim: create empty dataframe with required dimensions.
    
        # parameters:
        #   self: class. 
    
        #return: IF success: Empty dataframe with required dimensions. ELSE: -.
        """
            
        try:
            
            if ((self.ncols > 0) and (self.nindex > 0)):
                
                self.df = pd.DataFrame(columns = range(self.ncols), index = range(self.nindex))
                
            else:
                
                raise ValueError
            
        except (Exception, ValueError, TypeError):
            
            print("Invalid dimensions!")
      

    def __assign_col(self, icols): 

        """ __assign_col: fill column with index icol.
        
        # parameters:
        #   self: class. 
        #   icols: index of the column to fill. Type: int.
    
        # return: IF success: TRUE. ELSE: FALSE
        """

        try:
            
            if ((len(self.values.keys()) >= self.ncols) and
                (len(self.values[icols]) == self.nindex)):
                
                self.df[icols] = self.values[icols]
                return True
                
            else:
                
                raise ValueError
            
        except (Exception, ValueError, TypeError):
            
            print("Invalid column!")
            return False
            

    def __assign_values(self): 

        """ __assign_values: fill dataframe by columns.
    
        # parameters:
        #   self: class. 
    
        # return: IF success: Filled dataframe with ncols. ELSE: -.
        """
        
        testCol = False

        try:
            for idCol in range(self.df.shape[1]):

                testCol = self.__assign_col(idCol)

                if testCol is False:
                    continue
                    
        except (Exception, ValueError, TypeError):
            
            print("Invalid value!")

        del testCol

    
    def fill_df(self, name, ncols, nindex, values):
        self.__add__attributes(name, ncols, nindex,values)
        self. __assign_dim()
        self.__assign_values()

        
    def  __del__(self):
        del self.name
        del self.ncols
        del self.nindex
        del self.values 
        del self.df
        del self

