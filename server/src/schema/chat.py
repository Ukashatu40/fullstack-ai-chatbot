
from datetime import datetime
from pydantic import BaseModel, Field # type: ignore
from typing import List, Optional
from uuid import UUID
import uuid


class Message(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    msg: str
    timestamp: str = Field(default_factory=lambda: str(datetime.now()))


class Chat(BaseModel):
    token: str
    messages: List[Message]
    name: str
    session_start: str = Field(default_factory=lambda: str(datetime.now()))