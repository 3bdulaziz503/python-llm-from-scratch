import torch
import numpy as np
import matplotlib

print("PyTorch:", torch.__version__)
print("NumPy:", np.__version__)
print("Matplotlib:", matplotlib.__version__)

x = torch.tensor([1, 2, 3, 4, 5])

print("Tensor:", x)
print("Tensor multiplied by 2:", x * 2)

print("CUDA Available:", torch.cuda.is_available())