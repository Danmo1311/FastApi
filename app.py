import uvicorn
from fastapi import FastAPI
from Routes.Alpha import Alpha

app = FastAPI()
app.include_router(Alpha)
posts = []


@app.get('/')
def read_root():
    return {"Welcome": "Welcome to REST my API"}


@app.get('/posts')
def get_posts():
    return posts


@app.post('/post')
def save_post(post):
    return "recibido"
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        #port=get_settings().DEV_SRV_PORT,
        reload=True,
        debug=True,
    )
