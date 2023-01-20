import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from authtoken import auth_token
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

app = tk.Tk()
app.geometry('1280x720')
app.title('TextToImage App')
ctk.set_appearance_mode('dark')

prompt = ctk.CTkEntry(app, height=40, width=1280, text_color='black', fg_color='white')
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=1080, width=600)
lmain.place(x=10, y=110)

modelid = 'CompVis/stable-diffusion-v1-4'
device = 'cuda'
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision='fp16', torch_dtype=torch.float16, use_auth_token=auth_token)
pipe.to(device)

def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.0)['sample'][0]

    img = ImageTk.PhotoImage(image)
    image.save('generatedimage.png')
    lmain.configure(image=img)

trigger = ctk.CTkButton(app, height=40, width=120, text_color='black', fg_color='red', command=generate)
trigger.configure(text='Generate')
trigger.place(x=580, y=60)

app.mainloop()