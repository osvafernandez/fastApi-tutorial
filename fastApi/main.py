from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'hola': 'mundo'}


@app.get('/url')
async def root():
    return {"url_curso": "https://mouredev.com/python"}
