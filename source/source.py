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
                                                'case14','case24_ieee_rts','case30','case_ieee30',
                                                'case33bw','case39','case57','case89pegase',
                                                'case118','case145','case_illinois200','case300',
                                                'case1354pegase','case1888rte','case2848rte','case2869pegase',
                                                'case3120sp','case6470rte','case6495rte','case6515rte',
                                                'case9241pegase','GBnetwork','GBreducednetwork','iceland'])):
            
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
                dtNew = pandapower.networks.case9()
            case 'case9':
                dtNew = pandapower.networks.case14()
            case 'case14':
                dtNew = pandapower.networks.case24_ieee_rts()
            case 'case24_ieee_rts':
                dtNew = pandapower.networks.load_breast_cancer()
            case 'case30':
                dtNew = pandapower.networks.load_iris()
            case 'case_ieee30':
                dtNew = pandapower.networks.load_diabetes()
            case 'case33bw':
                dtNew = pandapower.networks.load_digits()
            case 'case39':
                dtNew = pandapower.networks.load_wine()
            case 'case57':
                dtNew = pandapower.networks.load_linnerud()
            case 'case89pegase':
                dtNew = pandapower.networks.load_breast_cancer()
            case 'case118':
                dtNew = pandapower.networks.load_iris()
            case 'case145':
                dtNew = pandapower.networks.load_diabetes()
            case 'case_illinois200':
                dtNew = pandapower.networks.load_digits()
            case 'case300':
                dtNew = pandapower.networks.load_wine()
            case 'case1354pegase':
                dtNew = pandapower.networks.load_linnerud()
            case 'case1888rte':
                dtNew = pandapower.networks.load_breast_cancer()
            case 'case2848rte':
                dtNew = pandapower.networks.load_iris()
            case 'case2869pegase':
                dtNew = pandapower.networks.load_diabetes()
            case 'case3120sp':
                dtNew = pandapower.networks.load_digits()
            case 'case6470rte':
                dtNew = pandapower.networks.load_wine()
            case 'case6495rte':
                dtNew = pandapower.networks.load_linnerud()
            case 'case6515rte':
                dtNew = pandapower.networks.load_breast_cancer()
            case 'case9241pegase':
                dtNew = pandapower.networks.load_breast_cancer
            case 'GBnetwork':
                dtNew = pandapower.networks.load_breast_cancer()
            case 'GBreducednetwork':
                dtNew = pandapower.networks.load_breast_cancer()
            case 'iceland':
                dtNew = pandapower.networks.load_breast_cancer()

    del testFlag
    return dtNew
