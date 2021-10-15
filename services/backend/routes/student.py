from typing import List

from bson import ObjectId
from fastapi import APIRouter
from pymongo import ReturnDocument
from starlette import status
from fastapi.exception_handlers import HTTPException

from config.db import student_collection
from models.student import CreateStudent, UpdateStudent, ResponseInDb
from schemas.student import list_of_students_entity, student_entity

student_router = APIRouter()


@student_router.get('/students', response_model=List[ResponseInDb])
async def find_all_students():
    result = student_collection.find()
    return list_of_students_entity(result)


@student_router.get('/students/{student_id}', response_model=ResponseInDb)
async def find_student_by_id(student_id: str):
    result = student_collection.find_one({'_id': ObjectId(student_id)})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'student with id {student_id} not found!'
        )
    return student_entity(result)


@student_router.post('/students', status_code=status.HTTP_201_CREATED, response_model=ResponseInDb)
async def create_student(student: CreateStudent):
    id = student_collection.insert_one(student.dict()).inserted_id
    return student_entity(student_collection.find_one({'_id': id}))


@student_router.put('/students/{student_id}', response_model=ResponseInDb)
async def update_student(student_id: str, student: UpdateStudent):
    updated = student_collection.find_one_and_update(
        {'_id': ObjectId(student_id)},
        {'$set': student.dict()},
        return_document=ReturnDocument.AFTER
    )
    return student_entity(updated)


@student_router.delete('/students/{student_id}', status_code=status.HTTP_200_OK, response_model=ResponseInDb)
async def delete_student(student_id: str):
    deleted = student_collection.find_one_and_delete({'_id': ObjectId(student_id)})
    return student_entity(deleted)
