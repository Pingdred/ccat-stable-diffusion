from pydantic import BaseModel, Field
from cat.mad_hatter.decorators import plugin

class MySettings(BaseModel):
    api_key: str
    engine: str = "stable-diffusion-xl-1024-v1-0"
    height: int = Field(default=1024, title="Image Height")
    width: int = Field(default=1024, title="Image width")
    steps: int = 10

@plugin
def settings_schema():  
    return MySettings.schema()