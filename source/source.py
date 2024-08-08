import typing as tp

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
