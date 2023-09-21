#!/usr/bin/env bash

set -e

MODEL_NAME="stable-diffusion-xl-base-1.0" # ie.) stable-diffusion-v1-4 OR stable-diffusion-xl-base-1.0
BUCKET_NAME="$(cat ../terraform/bucket-name.txt)"

cd ../

# copy code into model folder
cp -r sagemaker/code ${MODEL_NAME}

cd ${MODEL_NAME}
rm model.tar.gz 2> /dev/null || true
tar cvf model.tar.gz --use-compress-program=pigz ./*
aws s3 cp model.tar.gz "s3://${BUCKET_NAME}/${MODEL_NAME}.tar.gz"
rm model.tar.gz

cd ../sagemaker
