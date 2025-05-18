# import torch

# checkpoint_path = '/Users/elias/Dev/yolov6-object-detector/yolov6n_seg.pt'
# checkpoint = torch.load(checkpoint_path, map_location='cpu')

# print(checkpoint.keys())

import sys
sys.path.append('/Users/elias/Dev/yolov6-object-detector/YOLOv6')


import yolov6.models.heads.effidehead_fuseab_seg
print(hasattr(yolov6.models.heads.effidehead_fuseab_seg, 'Detect'))
