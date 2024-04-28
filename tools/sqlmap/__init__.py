#!/usr/bin/python3

import subprocess

from tools import Tool


# Sqlmap
class Sqlmap(Tool):

    def __init__(self):
        """
        Initialize Sqlmap.
        """
        # Initialize Tool
        super().__init__(
            name="Sqlmap", 
            description="Detect and exploit SQL injection vulnerabilities.",
            usecase="This is useful for when you need to detect and exploit SQL injection vulnerabilities in a web application.",
            parameters={
                "cmd": "The sqlmap command to execute."
            }
        )
    
    def run(self, cmd):
        """
        This function will execute the provided command.
        """
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            cmd_return = output.decode('utf-8').strip()
            
        except Exception as e:
            return f"An error occured executing the command: {e}"    
            
        return f"The command was executed successfully. It returned {cmd_return if cmd_return else 'nothing, indicating that you achieved your goal. That means, that you can now continue with the next task or respond back to the human if there are no further steps to do.'}"