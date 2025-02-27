import torch

ckpt_path = "/home/yanjieze2/xchen47/OpenHomie/HomieRL/legged_gym/logs/experiment_1/Feb19_15-21-15_my_policy/model_16400.pt"
checkpoint = torch.load(ckpt_path, map_location="cpu")  
print(checkpoint.keys())  
