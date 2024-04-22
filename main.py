# from src.get_posts import get_posts
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


from flask import Flask, request, jsonify
from src.get_posts import get_posts

app = Flask(__name__)


class About:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class Msg:
    def __init__(self, msg):
        self.msg = msg


@app.route("/")
def get_index():
    msg = Msg("¡Bienvenido!")
    return jsonify(msg.__dict__)


@app.route("/api/posts/")
def get_user_posts():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Nombre de usuario no proporcionado"})
    try:
        data_total = get_posts(username)
        if isinstance(data_total, str):
            return jsonify({"error": "Usuario no encontrado"})
        return jsonify(data_total)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/stories/")
def get_user_stories():
    msg = Msg("En construcción")
    return jsonify(msg.__dict__)


@app.route("/api/about/")
def get_about():
    about = About(
        title="Acerca de instaPy",
        description="¡Sitio para ver contenido como: fotos, videos, reels, Instagram de forma anónima XD!",
    )
    return jsonify(about.__dict__)


if __name__ == "__main__":
    app.run()
