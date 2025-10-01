import os
from crewai import Agent, LLM
from crewai_tools import FileReadTool


model = os.getenv("ANALYST_AGENT_LLM")
temperature = float(os.getenv("ANALYST_AGENT_TEMPERATURE"))

llm = LLM(
         model=model,
         temperature=temperature
)

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyst gathered information to extract key insights ,patterns, and conclysions",
    backstory=(
               "You are a skilled data analyst with expertise in synthesizing complex "
                "information into actionable insights. You excel at identifying patterns, trends, "
                "and key findings from research data."
    ),
    llm=llm,
    verbose=True,
    tools=[FileReadTool()]
)
