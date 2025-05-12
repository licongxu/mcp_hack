from autogen import GroupChat, GroupChatManager

def create_manager(user, agents, llm_cfg, max_round: int = 3, send_introductions: bool = True):
    chat_room = GroupChat(
        agents=[user] + agents,
        messages=[],
        max_round=max_round,
        send_introductions=send_introductions,
    )
    return GroupChatManager(groupchat=chat_room, llm_config=llm_cfg)