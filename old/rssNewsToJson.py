import json
from src.data import rss

a = rss.News("python", "teste", "code", "Titulo do codigo", "pt_BR")

print(json.dumps(a.__dict__))
