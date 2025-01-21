from fastapi import APIRouter, Depends

route = APIRouter()

controller_anonymous = APIRouter()
controller = APIRouter(dependencies=[Depends()]) # add authorization