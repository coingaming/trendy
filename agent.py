from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from trends import get_trending_repos
from langchain.agents import AgentType, initialize_agent

llm = ChatOpenAI(temperature=0)

tools = [
    Tool.from_function(
        func=get_trending_repos,
        name="Get trending repos",
        description="useful for when you need to get a list of today's trending repos on github, where stars_per_day is the number of stars the repo has received in the last 24 hours",
    ),
]

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run(
    "What are the trending repos with the most stars on github today?"
)