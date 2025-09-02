import traceback

from agents import Runner, gen_trace_id, trace

from .search_agent import search_agent


class SupervisorAgent:
    async def search(self, item) -> str | None:
        """Perform a search for the query"""
        input = f"Search term: {item}"
        print(input)
        try:
            agent = await search_agent()
            result = await Runner.run(
                agent,
                input,
            )
            print(result.final_output)
            return str(result.final_output)
        except Exception as e:
            print(traceback.format_exc())
            return None

    async def run(self, query: str):
        trace_id = gen_trace_id()
        with trace("supervisor", trace_id=trace_id):
            search_results = await self.search(query)
            return search_results
