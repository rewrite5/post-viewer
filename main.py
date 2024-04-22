from src.get_posts import get_posts
from pydantic import BaseModel
from fastapi import FastAPI, Query
# import uvicorn

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


# @app.get("/api/posts/")
# async def get_user_posts(
#     username: str = Query(..., description="Username of the user")
# ):
#     try:
#         data_total = get_posts(username)
#         if isinstance(data_total, str):
#             return {"error": "User not found"}
#         return data_total
#     except Exception as e:
#         return {"error": str(e)}


@app.get("/api/posts/{username}")
async def get_user_posts(username: str):
    try:
        data_total = get_posts(username)
        if isinstance(data_total, str):
            return {"error": "Usuario no encontrado"}
        return data_total
    except Exception as e:
        return {"error": str(e)}


@app.get("/api/stories/")
async def get_user_stories(
    # username: str = Query(..., description="Username of the user")
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
