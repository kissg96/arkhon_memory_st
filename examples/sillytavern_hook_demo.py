# arkhon_memory_st/examples/sillytavern_hook_demo.py
# Simulates storing and retrieving memories for a character.
# This is a simple demonstration of how to use the SillyTavern bridge

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

if __name__ == "__main__":
    main()
