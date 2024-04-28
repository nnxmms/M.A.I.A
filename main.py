#!/usr/bin/python3

# M.A.I.A
from maia import MAIA

# Tools
from tools import Bash
from tools import GoogleSearch
from tools import Interpreter
from tools import Nmap
from tools import Sqlmap

# Regular imports
from dotenv import load_dotenv
import os

# Main function
def main():
    """
    This function starts M.A.I.A.
    """
    # Initialize tools
    tools = [
        GoogleSearch(
            google_cse_id=os.environ.get("GOOGLE_CSE_ID"),
            google_api_key=os.environ.get("GOOGLE_API_KEY")
        ),
        Bash(),
        Interpreter(),
        Nmap(),
        Sqlmap()
    ]

    # Run M.A.I.A.
    maia = MAIA(tools=tools)
    maia.run()

if __name__ == '__main__':
    
    # Load environment variables from .env file
    load_dotenv('.env')
    
    # Run main
    os.system("clear")
    main()