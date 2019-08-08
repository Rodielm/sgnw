
from typing import (Optional, List)
from datetime import date
from pydantic import BaseModel


class NotifyStateBase(BaseModel):
    name: str
    
class NotifyStateInResponse(NotifyStateBase):
    pass

class NotifyStateInDB(NotifyStateBase):
    pass

class NotifyStateInUpdate(NotifyStateBase):
    pass

class ManyNotifyStateInResponse(NotifyStateBase):
    notifyStates: List[NotifyStateBase]
