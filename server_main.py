import logging
from typing import List

import numpy as np
from fastapi import FastAPI

from search import ImageSearcher

app = FastAPI()
app.state.searcher = ImageSearcher()


@app.get('/find_text', response_model=List[str])
async def find_text(query: str) -> List[str]:
    result = app.state.searcher.search(query).squeeze().astype(np.int32).tolist()
    logging.info(str(result))
    return result


@app.get('/healthz', response_model=str)
async def health_check() -> str:
    return 'OK'
