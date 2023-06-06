from properties import GraphProperties
import networkx as nx


GraphProperties(nx.read_edgelist("Data/aves-sparrow-social-2010.edges",
                                 nodetype=int, data=(("Type", str),)),
                )

# GraphProperties(nx.read_edgelist("Data/3elt.mtx",
#                                  nodetype=int, data=(("Type", str),)),
#                 )

# GraphProperties(nx.read_edgelist("Data/bcspwr10.mtx",
#                                  nodetype=int, data=(("Type", str),)),
#                 )

# GraphProperties(nx.read_edgelist("Data/USpowerGrid.mtx",
#                                  nodetype=int, data=(("Type", str),)),
#                 )

# GraphProperties(nx.read_edgelist("Data/uk.mtx",
#                                  nodetype=int, data=(("Type", str),)),
#                 )

# GraphProperties(nx.read_edgelist("Data/power.mtx",
#                                  nodetype=int, data=(("Type", str),)),
#                 )
