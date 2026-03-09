def get_web_search_tool():
    """Returns a dummy web search tool for local testing."""
    class DummyWebSearch:
        def invoke(self, query):
            return "Mock Web Search Results: The CEO was interviewed yesterday stating positive growth."
    return DummyWebSearch()
