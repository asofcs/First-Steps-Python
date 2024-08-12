import source.source as scr
#import networkx
#import pandapower


def main():
    # print network information
    network_info('case39', True, True, True,
                 True, True, True, True,
                 True)
    # run pf (See args in https://pandapower.readthedocs.io/en/latest/powerflow/ac.html)
    network_functions('case39', 'pf', ())
    
    # run topology - respect_switches=True, include_lines=False (See args in https://pandapower.readthedocs.io/en/latest/topology/create_graph.html)
    network_functions('case39', 'top', ())
  
if __name__ == "__main__":
    main()
