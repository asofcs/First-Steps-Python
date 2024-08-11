import pandapower
import typing 
#import numpy
#import pandas 
#import matplotlib.pyplot



def load_network(name: typing.Optional[str] = None,)-> net:
    
    """ Load network from the pandapower.networks package (Power System Test Cases)
    
    # parameters:
    #  name: name of network to import. Type: str.

    # return: IF success: network. ELSE: None
    """
    
    testFlag = False
    dtNew = None
    
    try:
        
        if (isinstance(name, str) and (name in ['case4gs','case6ww','case9',
                                                'case14','case30','case33bw',
                                                'case39','case57','case89pegase',
                                                'case118','case145','case300',
                                                'case1354pegase','case1888rte','case2848rte',
                                                'case2869pegase','case3120sp','case6470rte',
                                                'case6495rte','case6515rte','case9241pegase',
                                                'GBnetwork','GBreducednetwork','iceland'])):
            
            testFlag = True
        
        else:
            raise Exception

            
    except(Exception, ValueError, TypeError):
        print(f'Invalid dataset - {name} - (load_dataset)')

    if testFlag is True:
        match name:
            case 'case4gs':
                dtNew = pandapower.networks.case4gs()
            case 'case6ww':
                dtNew = pandapower.networks.case6ww()
            case 'case9':
                dtNew = pandapower.networks.case9()
            case 'case14':
                dtNew = pandapower.networks.case14()
            case 'case30':
                dtNew = pandapower.networks.case30()
            case 'case33bw':
                dtNew = pandapower.networks.case33bw()
            case 'case39':
                dtNew = pandapower.networks.case39()
            case 'case57':
                dtNew = pandapower.networks.case57()
            case 'case89pegase':
                dtNew = pandapower.networks.case89pegase()
            case 'case118':
                dtNew = pandapower.networks.case118()
            case 'case145':
                dtNew = pandapower.networks.case145()
            case 'case300':
                dtNew = pandapower.networks.case300()
            case 'case1354pegase':
                dtNew = pandapower.networks.case1354pegase()
            case 'case1888rte':
                dtNew = pandapower.networks.case1888rte()
            case 'case2848rte':
                dtNew = pandapower.networks.case2848rte()
            case 'case2869pegase':
                dtNew = pandapower.networks.case2869pegase()
            case 'case3120sp':
                dtNew = pandapower.networks.case3120sp()
            case 'case6470rte':
                dtNew = pandapower.networks.case6470rte()
            case 'case6495rte':
                dtNew = pandapower.networks.case6495rte()
            case 'case6515rte':
                dtNew = pandapower.networks.case6515rte()
            case 'case9241pegase':
                dtNew = pandapower.networks.case9241pegase()
            case 'GBnetwork':
                dtNew = pandapower.networks.GBnetwork()
            case 'GBreducednetwork':
                dtNew = pandapower.networks.GBreducednetwork()
            case 'iceland':
                dtNew = pandapower.networks.iceland()

    del testFlag
    return dtNew
