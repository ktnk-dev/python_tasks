import fastapi
import uvicorn
import corotune
import datetime
import functions
import importlib

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

api = fastapi.FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

class Run(BaseModel):
    inputs: list

@api.get('/')
def root():
    global corotune
    corotune = importlib.reload(corotune)
    db = functions.load_db()
    result = {}
    for k, v in db.items():
        result[k] = {
            'func': v,
            'inputs': functions.get_inputs(k),
            'code': functions.show_code(k, var = True)
        }
    return {
        'hash': functions.get_hash(),
        'base_url': 'https://informatics.msk.ru/mod/statements/view.php?chapterid=%s',
        'functions': result
    }


@api.post('/run/{num}')
def run(body: Run, num: int):
    global corotune
    corotune = importlib.reload(corotune)
    db = functions.load_db()
    start_time = datetime.datetime.now()
    result = eval(f'{db[num]}({", ".join(["body.inputs["+str(input_num)+"]" for input_num in range(len(body.inputs))])})')
    end_time = datetime.datetime.now() - start_time

    return {
        'result': result,
        'time': round(end_time.seconds + end_time.microseconds / 1_000_000, 5)
    }

uvicorn.run(api, host = '127.0.0.1', port = 12943)