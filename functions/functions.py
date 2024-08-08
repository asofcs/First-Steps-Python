def check_instance(var, xtype, verror):
    """
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
