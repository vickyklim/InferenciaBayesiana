# -*- coding: utf-8 -*-
from Historia import *

eventos = [ [["a"],["b"]],
            [["b"],["a"]] ]

h = Historia(eventos)
for _  in range(10):
  h.forward_propagation()
  h.backward_propagation()
h.posteriors()
