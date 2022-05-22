from pydantic import BaseModel
from typing import List, Optional

class RequestUser(BaseModel):
    email : Optional[str]
    username : Optional[str]
    password : Optional[str]

class CreateAccoutuser(BaseModel):
    main : Optional[RequestUser]
    role : Optional[str] = "T"

    