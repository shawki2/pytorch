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
