from typing import List

from fastapi import FastAPI

from search import ImageSearcher

app = FastAPI()
app.state.searcher = ImageSearcher()


@app.get('/find_text', response_model=List[dict])
async def find_text(query: str) -> List[dict]:
    result = app.state.searcher.search(query)
    return result


@app.get('/healthz', response_model=str)
async def health_check() -> str:
    return 'OK'
