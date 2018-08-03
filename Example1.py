# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py

from __future__ import print_function
import torch
elemEmpty = torch.empty(5, 3)
print('elemempty', elemEmpty)
elemRandum = torch.rand(5, 3)
print('==========')
print('elemrandum', elemRandum)
elemZero = torch.zeros(5, 3, dtype=torch.long)
print('==========')
print('elemZero', elemZero)
elemTensor = torch.tensor([5.5, 3])
print('==========')
print('elemTensor =', elemTensor)
elemN = torch.tensor([5.5, 3])
print(elemN)
print('==========')
# new_* methods take in sizes
elemN = elemN.new_ones(5, 3, dtype=torch.double)
print(elemN)
print('==========')
elemN = torch.randn_like(elemN, dtype=torch.float)    # override dtype!
print(elemN)                                      # result has the same size
print(elemN.size())
