from src.get_posts import get_posts
from pydantic import BaseModel
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


class About(BaseModel):
    title: str
    description: str


class Msg(BaseModel):
    msg: str


@app.get("/")
async def get_index():
    msg = Msg(msg="Welcome!")
    return msg


@app.get("/api/posts/")
async def get_user_posts(
    username: str = Query(..., description="Username of the user")
):
    data_total = get_posts(username)
    return data_total


@app.get("/api/stories/")
async def get_user_stories(
    username: str = Query(..., description="Username of the user")
):
    msg = Msg(msg="Under construction")
    return msg


@app.get("/api/about/")
async def get_about():
    about = About(
        title="About instaPy",
        description="Site to view content such as: photos, videos, reels, instagram anonymously XD!",
    )
    return about


if __name__ == "__main__":
    pass
    # uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn main:app --reload
