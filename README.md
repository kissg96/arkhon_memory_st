# Arkhon-Memory-ST

This is a drop-in SillyTavern memory bridge using [`arkhon-memory`](https://github.com/kissg96/arkhon-memory).**  
Adds persistent memory with time-decay + reuse scoring to your character chats — lightweight, local-first, and extensible.

If you hit integration issues, open an issue or DM me i'll try to help — but i hope most of you will find this plug-and-play

---

## Installation

```bash
pip install arkhon-memory-st
```

---

## What This Does?

This bridge lets SillyTavern periodically:

- Store important conversation events into long-term memory
- Retrieve relevant past context using keyword + time-weighted scoring

---

## Integration Guidance

- Call `store_memory(...)` **after every user or assistant message** you want to remember.
- Call `retrieve_memory(...)` **before generating a new LLM reply**, using the latest user message(s) as context.
- Insert the retrieved snippets directly into the prompt context for best results.

This module does not manage timing or injection for you — it provides plug-and-play hooks for any LLM/chat tool to wire in as needed.

---

## Usage example

```python
from arkhon_st.sillytavern_bridge import store_memory, retrieve_memory

def main():
    character = "Alice"
    session = "session-xyz"
    store_memory(character, "You told me yesterday that you love hiking.", role="assistant", session_id=session)
    store_memory(character, "We discussed your favorite foods: pizza and ramen.", role="user", session_id=session)
    store_memory(character, "You wanted to visit the mountains next summer.", role="assistant", session_id=session)

    user_now = "What do you remember about my travel plans?"
    memories = retrieve_memory(character, user_now, n_results=2)
    print(f"Top memories for {character}:")
    for idx, mem in enumerate(memories, 1):
        print(f"{idx}. {mem}")


