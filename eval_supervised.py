gpu_mode: True
deformation_model: NDP


use_ldmk: True
ldmk_config: "./correspondence/configs/correspondence.yaml"

num_workers: 4
batch_size: 1
augment_noise: False


use_depth: False

w_ldmk: 1
w_cd: &w_cd 0.0
w_reg: &w_reg 0.0

trunc_cd : 0.25



# motion representation
motion_type : &motion_type  "SE3" # option  [ "Sim3", "SE3", "sflow"]
rotation_format : &rotation_format  "axis_angle" # options [ "6D", "quaternion", "axis_angle", "euler"]

#optimization
iters: &iters 500
lr: 0.01
momentum: 0.9
weight_decay: 0.0001
max_break_count: 15
break_threshold_ratio: 0.001


# threshold of inlier match
inlier_thr : &inlier_thr 0.3
reject_outliers: &reject_outliers True

samples: &samples 2000

#pyramid configuration
m : &m 10
k0 : &k0 -8
depth: &depth 3
width: &width 128
act_fn: relu




#dataset
data_root : "/content/DeformationPyramid/data/4DMatchHumanoid"
split: { 'test': "test" }

#experiment
folder: confidence_ab
