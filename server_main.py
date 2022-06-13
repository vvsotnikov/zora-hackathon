from typing import List

from PIL import Image
from fastapi import FastAPI, UploadFile, File

from search import ImageSearcher

app = FastAPI()
app.state.searcher = ImageSearcher()


@app.get('/find_text', response_model=List[dict])
async def find_text(query: str) -> List[dict]:
    result = app.state.searcher.search(query)
    return result


@app.post('/find_image', response_model=List[dict])
async def find_image(image: UploadFile = File(...)) -> List[dict]:
    image = Image.open(image.file)
    result = app.state.searcher.search_image(image)
    return result


@app.get('/healthz', response_model=str)
async def health_check() -> str:
    return 'OK'
