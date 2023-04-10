import torch
import torch.nn  as nn
import torch.nn.functional as F

torch.manual_seed(1)

x_train = torch.FloatTensor([[1],[2],[3]])
y_train = torch.FloatTensor([[2],[4],[6]])

model = nn.Linear(in_features=1, out_features=1)

print(list(model.parameters()))