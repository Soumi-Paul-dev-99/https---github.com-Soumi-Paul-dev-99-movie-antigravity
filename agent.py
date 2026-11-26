
from google.antigravity import Agent, LocalAgentConfig
from dotenv import load_dotenv
import os
import asyncio

from tools import *

load_dotenv()

# Agent Configuration
config = LocalAgentConfig(

    api_key=os.getenv("GEMINI_API_KEY"),

    model="gemini-3.5-flash-lite",

    tools=[
        showAllMovies,
        showMoviesByMultiplex,
        showMovieByGenre
    ],

    system_instructions="""
    You are a Movie Automation AI Assistant.

    Your job is to provide movie details
    using the available Python tools.

    Rules:

    1. If user asks for all movies,
       call showAllMovies().

    2. If user asks movies by multiplex,
       call showMoviesByMultiplex().

    3. If user asks movies by genre,
       call showMovieByGenre().

    4. Always use the database tools
       to get movie information.

    5. Never create fake movie information.

    6. Show movie ID, genre, time,
       hall ID and multiplex ID.

    7. Give simple and clear answers.
    """
)


# Agent Function
async def callAgent(user_input):

    async with Agent(config=config) as agent:

        response = await agent.chat(user_input)

        result = await response.text()

        return result


# Testing
async def main():

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = await callAgent(user_input)

        print("Agent:", result)


if __name__ == "__main__":
    asyncio.run(main())
