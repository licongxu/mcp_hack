from autogen import UserProxyAgent


def create_user_proxy(work_dir: str = "scratch"):
    return UserProxyAgent(
        name="user",
        system_message="A human traveller.",
        human_input_mode="TERMINATE",
        code_execution_config={
            "use_docker": False,
            "work_dir": work_dir,
            "last_n_messages": 0,
        },
    )