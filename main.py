import source.source as scr
#import networkx
#import pandapower


def main():
    # print network information
    network_info('case39', True, True, True,
                 True, True, True, True,
                 True)
    # run pf
    network_functions('case39', 'pf', ())
    
    # run topology
    network_functions('case39', 'top', ())
  
if __name__ == "__main__":
    main()
