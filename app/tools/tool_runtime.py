"""
Tool runtime
"""

from pydantic import BaseModel

class ToolSchema(BaseModel):
    base_url: str
    api_key: str
