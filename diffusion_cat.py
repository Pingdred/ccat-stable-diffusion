import os
import base64
import requests
from cat.mad_hatter.decorators import tool, hook
import asyncio
from cat.log import log

api_host = os.getenv('API_HOST', 'https://api.stability.ai')

if not os.path.exists("cat/static/stable_diffusion_images/"):
    os.mkdir("cat/static/stable_diffusion_images/")

async def generate_image(prompt, cat, loop):
    settings = settings = cat.mad_hatter.plugins["ccat-stable-diffusion"].load_settings()
    api_key = settings["api_key"]
    engine = settings["engine"]
    height = settings["height"]
    width = settings["width"]

    if api_key is None:
        raise Exception("Missing Stability API key.")

    # response = requests.post(
    #     f"{api_host}/v1/generation/{engine}/text-to-image",
    #     headers={
    #         "Content-Type": "application/json",
    #         "Accept": "application/json",
    #         "Authorization": f"Bearer {api_key}"
    #     },
    #     json={
    #         "text_prompts": [
    #             {
    #                 "text": prompt
    #             }
    #         ],
    #         "cfg_scale": 7,
    #         "height": height,
    #         "width": width,
    #         "samples": 1,
    #         "steps": 10,
    #     },
    # )

    # if response.status_code != 200:
    #     raise Exception("Non-200 response: " + str(response.text))

    # data = response.json()

    # image = data["artifacts"][0]
    # with open(f"{cat.get_static_path()}stable_diffusion_images/v1_txt2img.png", "wb") as f:
    #     f.write(base64.b64decode(image["base64"]))

    log.critical(f"<img src='{cat.get_static_url()}/stable_diffusion_images/v1_txt2img.png' />")

    loop.close()


@tool(return_direct=True)
def sd_generate_image(prompt, cat):
    """Use this tool to generate/draw an image. Input is the prompt to generate the image."""
    
    loop = asyncio.new_event_loop()
    loop.run_until_complete(generate_image(prompt, cat, loop))

    return "I'm generating the image, I'll send it to you as soon as it's ready"
    
