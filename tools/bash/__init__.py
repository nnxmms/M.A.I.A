#!/usr/bin/python3

import subprocess

from tools import Tool


# Bash
class Bash(Tool):

    def __init__(self):
        """
        Initialize Bash.
        """
        # Initialize Tool
        super().__init__(
            name="Bash", 
            description="Executes any bash command.",
            usecase="This is useful for when you need to save, read or execute something on the humans machine.",
            parameters={
                "cmd": "The bash command that should be executed."
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