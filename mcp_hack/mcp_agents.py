# mcp_agents.py  –  docker‑free version
from autogen import ConversableAgent, GroupChat, GroupChatManager, LLMConfig, UserProxyAgent

llm_cfg = LLMConfig(api_type="openai", model="gpt-4o-mini", temperature=0.3)

MAP_PROMPT  = "You are MapAgent. Only answer map / route questions; otherwise say DEFER_TO_PLANNER."
BOOK_PROMPT = "You are BookingAgent. Only answer accommodation questions; otherwise say DEFER_TO_PLANNER."
PLAN_PROMPT = (
    "You are Planner. Decide who should speak next, gather info, then output a plan headed with ### Final Plan."
)

with llm_cfg:
    planner       = ConversableAgent("planner",       PLAN_PROMPT)
    map_agent     = ConversableAgent("map_agent",     MAP_PROMPT)
    booking_agent = ConversableAgent("booking_agent", BOOK_PROMPT)

# ── docker‑free user proxy ────────────────────────────────────────────────────
user = UserProxyAgent(
    name="user",
    system_message="A human traveller.",
    human_input_mode="TERMINATE",       # auto‑run; no interactive input
    code_execution_config={
        "use_docker": False,            # ← disable docker
        "work_dir":   "scratch",        # temporary folder for any code
        "last_n_messages": 0,           # (optional) no code execution needed here
    },
)

chat_room = GroupChat(
    agents=[user, planner, map_agent, booking_agent],
    messages=[],
    max_round=12,
    send_introductions=True,
)

manager = GroupChatManager(groupchat=chat_room, llm_config=llm_cfg)

if __name__ == "__main__":
    user.initiate_chat(
        recipient=manager,
        message=(
            "Plan a 3‑day city break in Barcelona for two adults, 5–7 July 2025. "
            "We love Gaudí architecture and vegetarian food. Budget €150 pp per night."
        ),
    )
