from pydantic import BaseModel
from typing import Optional
import json


class Task(BaseModel):
    name: str
    description: Optional[str] = ""
    version: str = "0.1.0"
    author: Optional[str] = ""
    author_email: Optional[str] = ""
    author_url: Optional[str] = ""
    license: Optional[str] = ""
    url: Optional[str] = ""
    tags: Optional[list[str]] = []
    readme: Optional[str] = "README.md"

print(json.dumps(Task.model_json_schema(), indent=2))