from fastapi import APIRouter
from config.db import conn
from models.Alpha import alpha
Alpha = APIRouter()
@Alpha.get("/alpha")
def get_alpha():
    return conn.excute(alpha.select().fetch_all())
@Alpha.get("/")
def helloworld():
    return "hello World"
@Alpha.get("/")
def helloworld():
    return "hello World"
@Alpha.get("/")
def helloworld():
    return "hello World"
