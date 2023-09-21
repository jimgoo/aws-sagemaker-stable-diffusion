import os
from pathlib import Path

CURR_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

with open(CURR_PATH / ".." / "terraform" / "sagemaker-role-arn.txt", "r") as f:
    sagemaker_role = f.read()

with open(CURR_PATH / ".." / "terraform" / "bucket-name.txt", "r") as f:
    bucket_name = f.read()

# this is the name of the endpoint in the AWS console
RESOURCE_NAME = "huggingface-pytorch-inference"

MODEL_NAME = 'stable-diffusion-xl-base-1.0'

MODEL_PARAMS = {
    "model_data": f"s3://{bucket_name}/sdv1-4_model.tar.gz",
    # "model_data": f"s3://{bucket_name}/{MODEL_NAME}.tar.gz",
    "name": RESOURCE_NAME,
    "role": sagemaker_role,
    "transformers_version": "4.12",
    "pytorch_version": "1.9",
    "py_version": "py38",
}

# Hub Model configuration. https://huggingface.co/models
## DOES NOT WORK WITH text-to-image!
# hub = {
#   'HF_MODEL_ID': 'stabilityai/stable-diffusion-xl-base-1.0',
#   'HF_TASK': 'text-to-image'
# }

# hub = {
#   'HF_MODEL_ID': 'CompVis/stable-diffusion-v1-4', #'stabilityai/stable-diffusion-xl-base-1.0',
#   'HF_TASK': 'text-to-image'
# }

# MODEL_PARAMS = {
#     "name": RESOURCE_NAME,
#     "role": sagemaker_role,
#     "transformers_version": "4.12",
#     "pytorch_version": "1.9",
#     "py_version": "py38",
#     "env": hub,
# }
