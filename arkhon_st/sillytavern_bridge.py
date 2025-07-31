# arkhon_memory_st/sillytavern_bridge.py
# Defines functions to store and retrieve memory for a character in SillyTavern.
# This module uses the arkhon_memory package to manage memory entries.

from datetime import datetime
from arkhon_memory.memory_hub import MemoryHub
from arkhon_st.st_schemas import STMemoryItem

# Choose a SillyTavern-specific memory file or allow path injection
_memory = MemoryHub("sillytavern_memory.json")
    
# Store a message in memory for a character.
# You can call this function after each user input or at specific intervals.
# It creates a memory item with the character's name as a tag and stores it in the memory hub.

def store_memory(
    character: str,
    user_input: str,
    tags: list[str] = None,
    role: str = None,
    session_id: str = None
):

    if tags is None:
        tags = []
    item = STMemoryItem(
        content=user_input,
        tags=tags + [character],
        timestamp=datetime.utcnow(),
        reuse_count=0,
        role=role,
        session_id=session_id
    )
    _memory.append(item)

# Retrieve memory for a character based on the current input.
# Use this function for querying the memory hub for relevant entries based on the current input.

def retrieve_memory(character: str, current_input: str, n_results: int = 3) -> list[str]:

    results = _memory.query(query_str=current_input, top_k=n_results)
    return [item.content for item in results]
