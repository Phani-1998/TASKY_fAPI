from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    profilePic: Optional[str] = None
    firstname: str
    lastname: Optional[str] = None
    mobilePhone: int
    officePhone: int
    employeeId: str
    userType: Optional[int] = 3
    role: int
    emailID: str
    businessEmail: str
    password: str
    auth: str
    createdBy: str
    createdOn: datetime = Field(default_factory=datetime.utcnow)
    companyId: str
    assignTo: str

class EmployeeUpdate(BaseModel):
    profilePic: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    mobilePhone: Optional[int] = None
    officePhone: Optional[int] = None
    employeeId: Optional[str] = None
    userType: Optional[int] = None
    role: Optional[int] = None
    emailID: Optional[str] = None
    businessEmail: Optional[str] = None
    password: Optional[str] = None
    auth: Optional[str] = None
    createdBy: Optional[str] = None
    createdOn: Optional[datetime] = None
    isDeleted: Optional[bool] = None
    isActive: Optional[bool] = None
    companyId: Optional[str] = None
    assignTo: Optional[str] = None