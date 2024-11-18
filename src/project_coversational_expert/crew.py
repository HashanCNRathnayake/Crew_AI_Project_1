# src/project_ai_reporter/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Chat():
    """Chat """

    @agent
    def coach(self) -> Agent:
        return Agent(
            config=self.agents_config['coach'],
            verbose=True
        )

    @task
    def coaching_task(self) -> Task:
        return Task(
            config=self.tasks_config['coaching_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Chat """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
