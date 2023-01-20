# Text-to-image-Generator
App to Generate Images from text using stable diffusion model.

We create an app to provide the user a prompt to provide text for image generation and then we use Stable Diffusion model to generate the image closely resembling that text.

Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input.

It is trained on 512x512 images from a subset of the LAION-5B database.

Note: If you are limited by GPU memory and have less than 10GB of GPU RAM available, please make sure to load the StableDiffusionPipeline in float16 precision.


URL to get authentiation token for stable diffusion: https://huggingface.co/docs/hub/security-tokens

Required libraries to install:
1. customtkinter
2. diffusers
3. huggingface-hub
4. Pillow
5. tokenizers
6. torch
7. torchaudio
8. torchvision
9. transformers
