import json
import time
import news

a = news.News("python", "teste", "code","Titulo do codigo", "pt_BR")

print(json.dumps(a.__dict__))
