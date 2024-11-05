from datetime import datetime
from typing import Optional
from beanie import Document

class UserModel(Document):
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
    createdOn: Optional[datetime] = datetime.now
    isDeleted: Optional[bool] = False
    isActive: Optional[bool] = True
    companyId: str
    assignTo: str

    class Settings: 
        collection="Employee_Details"