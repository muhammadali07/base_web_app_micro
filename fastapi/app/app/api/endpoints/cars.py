from os import error
from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from typing import Any, List

from starlette import responses
from config import settings
import schemas 
from crud import crudcar
from db import database

router = APIRouter()


@router.get("/getAll", response_model=schemas.msg.CarResponse)
async def get_all_cars()->Any:
    data = await crudcar.get_all()
    return { "data" : { "cars" : data } }

@router.post("/create",  response_model=schemas.msg.CreateOrUpdateResponse)
async def create_car(
    *,
    res: Response,
    req: schemas.appl.CarBase
)->Any:
    response = {
        "response_code": "01",
        "response_msg": "error",
        "message": "Internal Error"
    }

    data = await crudcar.create(obj_in=req)
    # raise Exception(data)

    if data:
        res.status_code=status.HTTP_201_CREATED
        response = {
            "message" : "create car was successfully",
            "data" : data
        }
    return response

@router.post("/delete/{id}", response_model=schemas.msg.BaseResponseModel)
async def delete_car(
    *,
    res: Response,
    id: int 
)-> Any:
    response = {
        "response_code": "01",
        "response_msg": "error",
        "message": "Internal Error"
    }

    data = await crudcar.get(id=id)
    if data is None:
        return {
            "response_code": "01",
            "response_msg": "warning",
            "message": "Car Not Found"
        }
    # raise Exception(data)
    await crudcar.delete(id=id)

    response = {
        "message" : "delete car was successfully",
    }
    return response


@router.post("/update",  response_model=schemas.msg.CreateOrUpdateResponse)
async def create_car(
    *,
    res: Response,
    req: schemas.appl.Car
)->Any:
    response = {
        "message_id": "01",
        "status": "error",
        "message": "Internal Error"
    }

    data_cek = await crudcar.get(id=req.id)
    if data_cek is None:
        return {
            "message_id": "02",
            "status": "warning",
            "message": "Car Not Found"
        }
    data = await crudcar.update(obj_in=req, db_obj=data_cek)
    # raise Exception(data)

    if data:
        res.status_code=status.HTTP_200_OK
        response = {
            "message" : "update car was successfully",
            "data" : data
        }
    return response