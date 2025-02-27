#  python legged_gym/legged_gym/scripts/train.py --task g1 --num_envs 128 --run_name my_policy --rl_device cuda:0 --sim_device cuda:0
# python legged_gym/legged_gym/scripts/train.py --task g1 --num_envs 4096 --headless --run_name my_policy --rl_device cuda:0 --sim_device cuda:0
# python /home/yanjieze2/xchen47/OpenHomie/HomieRL/legged_gym/legged_gym/scripts/train.py --task g1 --num_envs 4096 --headless --run_name my_policy --rl_device cuda:0 --sim_device cuda:0 --resume --checkpoint -1
# Train
python legged_gym/legged_gym/scripts/train.py --task g1 --num_envs 4096 --headless --run_name my_policy --rl_device cuda:0 --sim_device cuda:0 --resume --checkpoint -1
# Eval
python legged_gym/legged_gym/scripts/play.py --num_envs 1 --task g1 --resume