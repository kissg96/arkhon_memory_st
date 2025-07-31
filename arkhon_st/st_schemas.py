# arkhon_memory_st/st_schemas.py
# This module defines the schema extension used in the SillyTavern memory system.
# Using Pydantic for data validation and serialization.

from pydantic import BaseModel, Field
from arkhon_memory.schemas import MemoryItem
from typing import Optional

class STMemoryItem(MemoryItem):
    role: Optional[str] = None
    session_id: Optional[str] = None
