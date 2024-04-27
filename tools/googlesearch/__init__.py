#!/usr/bin/python3

from googleapiclient.discovery import build

from tools import Tool


# Google Search
class GoogleSearch(Tool):

    def __init__(self, google_cse_id, google_api_key):
        """
        Initialize GoogleSearch.
        """
        # Check for required parameters
        if not google_cse_id:
            raise ValueError("google_cse_id is required")
        if not google_api_key:
            raise ValueError("google_api_key is required")
        
        # Initialize Tool
        super().__init__(
            name="Google Search", 
            description="Search the internet using Google.",
            usecase="This is useful for when you need to answer questions about current events.",
            parameters={
                "search_term": "What you want to search for on Google."
            }
        )

        # Google parameters
        self._google_cse_id = google_cse_id
        self._google_api_key = google_api_key
    
    def run(self, search_term):
        """
        This function will search the given query on Google.
        """
        search_result = ""
        service = build("customsearch", "v1", developerKey=self._google_api_key)
        res = service.cse().list(q=search_term, cx=self._google_cse_id, num=10).execute()
        for result in res['items']:
            search_result = search_result + result['snippet']
        return search_result