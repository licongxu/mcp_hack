from .agents import MapAgent, BookingAgent, PlannerAgent
from .user import create_user_proxy
from .manager import create_manager
from autogen import LLMConfig


def plan_city_break(
    destination: str,
    start_date: str,
    end_date: str,
    adults: int = 2,
    preferences: str = "",
    budget_pp: float = 150.0,
    work_dir: str = "scratch",
):
    llm_cfg = LLMConfig(api_type="openai", model="gpt-4o-mini", temperature=0.3)
    planner = PlannerAgent(llm_cfg)
    map_agent = MapAgent(llm_cfg)
    booking_agent = BookingAgent(llm_cfg)
    user = create_user_proxy(work_dir)
    manager = create_manager(user, [planner, map_agent, booking_agent], llm_cfg)

    # Construct the user message
    message = (
        f"Plan a city break in {destination} for {adults} adults, "
        f"from {start_date} to {end_date}. We love {preferences}. "
        f"Budget €{budget_pp} pp per night."
    )
    user.initiate_chat(recipient=manager, message=message)
    return manager