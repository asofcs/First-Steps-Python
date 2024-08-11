import networkx
import pandapower
import typing




def load_network(name: typing.Optional[str] = None,)-> pandapower.auxiliary.pandapowerNet:

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


def network_info(name: typing.Optional[str] = None,
                 bus: typing.Optional[bool] = False,
                 load: typing.Optional[bool] = False,
                 gen: typing.Optional[bool] = False,
                 ext_grid: typing.Optional[bool] = False,
                 line: typing.Optional[bool] = False,
                 trafo: typing.Optional[bool] = False,
                 poly_cost: typing.Optional[bool] = False,
                 bus_geodata: typing.Optional[bool] = False):

    """ Print attribute from network if flag is True.

    # parameters:
    #  name: name of network. Type: str.
    #  bus: bus flag. Type: bool.
    #  load: load flag. Type: bool.
    #  gen: generators flag. Type: bool.
    #  ext_grid: external grids flag. Type: bool.
    #  line: lines flag. Type: bool.
    #  trafo: transformers flag. Type: bool.
    #  poly_cost:  cost functions flag. Type: bool.
    #  bus_geodata: geodata for buses flag. Type: bool.

    # return: -
    """

    testFlag = False
    dtNew = None

    try:
        dtNew = load_network(name)

        if (dtNew is not None):

            testFlag = True

        else:
            raise Exception

    except(Exception, ValueError, TypeError):
        print(f'Invalid network - {name} (network_info)')


    if testFlag is True:
        print('\n\tDATA DESCRIPTION:\n')

        if ((hasattr(dtNew, 'bus')) and (bus is True)):
            print('The bus data:\n', dtNew['bus'])

        if ((hasattr(dtNew, 'load')) and (load is True)):
            print('The load data:\n',dtNew['load'])

        if ((hasattr(dtNew, 'gen')) and (gen is True)):
            print('The generators data:\n',dtNew['gen'])

        if ((hasattr(dtNew, 'ext_grid')) and (ext_grid is True)):
            print('The external grids data:\n',dtNew['ext_grid'])

        if ((hasattr(dtNew, 'line')) and (ext_grid is True)):
            print('The lines data:\n',dtNew['line'])

        if ((hasattr(dtNew, 'trafo')) and (trafo  is True)):
            print('The transformers data:\n',dtNew['trafo'])

        if ((hasattr(dtNew, 'poly_cost')) and (poly_cost is True)):
            print('The cost functions\n',dtNew['poly_cost'])

        if ((hasattr(dtNew, 'bus_geodata')) and (bus_geodata is True)):
            print('The geodata for buses:\n',dtNew['bus_geodata'])

    del testFlag
    del dtNew


def network_functions(name: typing.Optional[str] = None,
                      func_name: typing.Optional[str] = None,
                      func_args: typing.Optional[tuple] = (),):
    """
    Run powerflow or topology.
    
    # parameters:
    #  name: name of the network. Type: str.
    #  func_name: function to run. Type: str
    #  func_args: arguments possible to the function. Type: tuple.
    #  Link powerflow: https://pandapower.readthedocs.io/en/latest/powerflow/ac.html
    #  Link topology: https://pandapower.readthedocs.io/en/latest/topology/searches.html
    #  Link networkx: https://networkx.org/documentation/stable/reference/introduction.html 

    # return: -
    """

    testFlag = False
    dtNew = None

    try:
        dtNew = load_network(name)

        if (dtNew is not None):

            testFlag = True

        else:
            raise Exception

    except(Exception, ValueError, TypeError):
        print(f'Invalid network - {name} (network_functions)')

    if testFlag is True:
        match func_name:
        
            case 'pf':

                print('\n\tRun Power Flow:\n')
                pandapower.runpp(dtNew, *func_args)
                print(dtNew.res_bus)

            case 'top':
                
                print('\n\tRun Topology:\n')
                mgraph = pandapower.topology.create_nxgraph(dtNew, *func_args)

                print('Edges:\n')
                try:
                  for id, val in enumerate(list(mgraph.edges)):
                    print(f'{id} -- {val}')
                except: pass

                print('Nodes:\n')
                try:
                  for id, val in enumerate(list(mgraph.nodes)):
                    print(f'{id} -- {val}')
                except: pass
    
    del testFlag
    del dtNew        
