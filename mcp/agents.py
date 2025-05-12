from autogen import ConversableAgent, LLMConfig


def default_llm_config():
    return LLMConfig(api_type="openai", model="gpt-4o-mini", temperature=0.3)


class MapAgent(ConversableAgent):
    def __init__(self, llm_cfg=None):
        llm_cfg = llm_cfg or default_llm_config()
        super().__init__(
            name="map_agent",
            system_message="You are MapAgent. Only answer map / route questions; otherwise say DEFER_TO_PLANNER.",
            llm_config=llm_cfg
        )


class BookingAgent(ConversableAgent):
    def __init__(self, llm_cfg=None):
        llm_cfg = llm_cfg or default_llm_config()
        super().__init__(
            name="booking_agent",
            system_message="You are BookingAgent. Only answer accommodation questions; otherwise say DEFER_TO_PLANNER.",
            llm_config=llm_cfg
        )


class PlannerAgent(ConversableAgent):
    def __init__(self, llm_cfg=None):
        llm_cfg = llm_cfg or default_llm_config()
        super().__init__(
            name="planner",
            system_message=(
                "You are Planner. Decide who should speak next, gather info, "
                "then output a plan headed with ### Final Plan."
            ),
            llm_config=llm_cfg
        )