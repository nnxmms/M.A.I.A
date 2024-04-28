#!/usr/bin/python3

import subprocess

from tools import Tool


# Ffuf
class Ffuf(Tool):

    def __init__(self):
        """
        Initialize Ffuf.
        """
        # Initialize Tool
        super().__init__(
            name="Ffuf", 
            description="Fuzz web applications for common files and directories.",
            usecase="This is useful for when you need to find hidden files or directories on a web server.",
            parameters={
                "cmd": "The ffuf command to execute."
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