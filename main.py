import source.source as scr
#import networkx
#import pandapower


def main():
    # print network information
    scr.network_info('case39', True, True, True,
                 True, True, True, True,
                 True)
    # run pf (See args in https://pandapower.readthedocs.io/en/latest/powerflow/ac.html)
    scr.network_functions('case39', 'pf', ())
    
    # run topology - respect_switches=True, include_lines=False (See args in https://pandapower.readthedocs.io/en/latest/topology/create_graph.html)
    scr.network_functions('case39', 'top', (True, False))
  
if __name__ == "__main__":
    main()
