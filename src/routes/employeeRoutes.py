import os
from uuid import uuid4
from fastapi import APIRouter, File, HTTPException, UploadFile, status
from src.models.employeeModel import UserModel
from src.schemas.employeeSchema import EmployeeCreate, EmployeeUpdate  # Import EmployeeUpdate
from datetime import datetime

employee_router = APIRouter()


@employee_router.post("/", response_model=UserModel)
async def create_employee(employee: EmployeeCreate):
    try:
        # Create new employee instance
        new_employee = UserModel(**employee.dict())
        await new_employee.insert()
        
        # Convert datetime to string for response
        new_employee.createdOn = new_employee.createdOn.isoformat()  # Convert to ISO format
        
        return new_employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@employee_router.get("/{id}", response_model=UserModel)
async def get_one_employee(id: str):
    try:
        employee = await UserModel.get(id)
        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@employee_router.get("/",response_model=list[UserModel])
async def get_all_employees():
    try:
        employees = await UserModel.find_all().to_list()
        return employees
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@employee_router.put("/{id}", response_model=UserModel)
async def update_employee(id: str, employee_data: EmployeeUpdate):
    try:
        employee = await UserModel.get(id)
        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        update_data= employee_data.dict(exclude_unset= True)
        await employee.update({"$set": update_data})
        updated_employee= await UserModel.get(id)
        return updated_employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@employee_router.delete("/{id}")
async def delete_employee(id: str):
    try:
        employee = await UserModel.get(id)
        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        await employee.delete()
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


