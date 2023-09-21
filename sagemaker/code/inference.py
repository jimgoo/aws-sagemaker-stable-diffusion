import io
import base64

import PIL
import torch
from diffusers import StableDiffusionPipeline
# from diffusers import DiffusionPipeline

PROMPT = "a photo of an astronaut riding a horse on mars"

def model_fn(model_dir):
    pipe = StableDiffusionPipeline.from_pretrained(model_dir, torch_dtype=torch.float16, revision="fp16")
    pipe = pipe.to("cuda")
    # pipe = DiffusionPipeline.from_pretrained(
    #     model_dir,
    #     torch_dtype=torch.float16,
    #     use_safetensors=True, 
    #     variant="fp16",
    # ).to("cuda")
    # #  pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead", fullgraph=True)
    return pipe

def predict_fn(data, pipe):
    prompt = data.pop("prompt", PROMPT)

    print(f'Starting inference with prompt: {prompt}')
    image: PIL.Image.Image = pipe(prompt).images[0]

    buffered = io.BytesIO()
    image.save(buffered, format='JPEG')
    return {'data': base64.b64encode(buffered.getvalue()).decode('utf-8'), 'prompt': prompt}
