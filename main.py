# from src.get_posts import get_posts
# from src.get_data import get_data_from_username
# from pydantic import BaseModel
# from fastapi import FastAPI, Query
# # import uvicorn

# app = FastAPI()


# class About(BaseModel):
#     title: str
#     description: str


# class Msg(BaseModel):
#     msg: str


# @app.get("/")
# async def get_index():
#     msg = Msg(msg="Welcome!")
#     return msg


# @app.get("/api/user/")
# async def validate_user(username: str = Query(..., description="Username of the user")):
#     try:
#         user = get_data_from_username(username)
#         return [user]
#     except Exception as e:
#         return {"error": str(e)}


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


# @app.get("/api/stories/")
# async def get_user_stories(
#     # username: str = Query(..., description="Username of the user")
# ):
#     msg = Msg(msg="Under construction")
#     return msg


# @app.get("/api/about/")
# async def get_about():
#     about = About(
#         title="About instaPy",
#         description="Site to view content such as: photos, videos, reels, instagram anonymously XD!",
#     )
#     return about


# if __name__ == "__main__":
#     pass


# from typing import List
# from fastapi import FastAPI, Query
# from pydantic import BaseModel
# from src.get_posts import get_posts
# from src.get_data import get_data_from_username

# app = FastAPI()


# class About(BaseModel):
#     title: str
#     description: str


# class Msg(BaseModel):
#     msg: str


# @app.get("/")
# async def get_index() -> Msg:
#     msg = Msg(msg="Welcome!")
#     return msg


# @app.get("/api/user/")
# async def validate_user(
#     username: str = Query(..., description="Username of the user")
# ) -> List[dict]:
#     try:
#         user = get_data_from_username(username)
#         return [user]
#     except Exception as e:
#         return [{"error": str(e)}]


# @app.get("/api/posts/")
# async def get_user_posts(
#     username: str = Query(..., description="Username of the user")
# ) -> List[dict]:
#     try:
#         data_total = get_posts(username)
#         if isinstance(data_total, str):
#             return [{"error": "User not found"}]
#         return data_total
#     except Exception as e:
#         return [{"error": str(e)}]


# @app.get("/api/stories/")
# async def get_user_stories() -> Msg:
#     msg = Msg(msg="Under construction")
#     return msg


# @app.get("/api/about/")
# async def get_about() -> About:
#     about = About(
#         title="About instaPy",
#         description="Site to view content such as: photos, videos, reels, instagram anonymously XD!",
#     )
#     return about

# if __name__ == "__main__":
#     pass


# from fastapi import FastAPI
# import httpx

# app = FastAPI()


# @app.get("/data/")
# async def get_data(page: int):
#     url = f"https://rickandmortyapi.com/api/character?page={page}"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response.json()

from typing import List
from flask import Flask, request, jsonify
from src.get_posts import get_posts
from src.get_data import get_data_from_username

app = Flask(__name__)


@app.route("/")
def get_index():
    return jsonify({"msg": "Welcome!"})


@app.route("/api/user/")
def validate_user():
    username = request.args.get("username")
    if username:
        try:
            user = get_data_from_username(username)
            return jsonify([user])
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Username parameter is missing"})


@app.route("/api/posts/")
def get_user_posts():
    username = request.args.get("username")
    if username:
        try:
            data_total = get_posts(username)
            if isinstance(data_total, str):
                return jsonify({"error": "User not found"})
            return jsonify(data_total)
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Username parameter is missing"})


@app.route("/api/stories/")
def get_user_stories():
    return jsonify({"msg": "Under construction"})


@app.route("/api/about/")
def get_about():
    about = {
        "title": "About instaPy",
        "description": "Site to view content such as: photos, videos, reels, instagram anonymously XD!",
    }
    return jsonify(about)


if __name__ == "__main__":
    app.run()
