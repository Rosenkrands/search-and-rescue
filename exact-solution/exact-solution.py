from docplex.mp.model import Model

vertices = [1,2,3]
arcs = {(1,2): 1, (1,3): 1, (2,1): 1}

# for i in enumerate(vertices):
#     for j in enumerate(vertices):
#         print(i, j)

tm = Model(name='transportation')
tm.print_information()