#!/usr/bin/python3

import subprocess

from tools import Tool


# Interpreter
class Interpreter(Tool):

    def __init__(self):
        """
        Initialize Interpreter.
        """
        # Initialize Tool
        super().__init__(
            name="Interpreter", 
            description="Executes a Python3 script.",
            usecase="This is useful for when you decide to execute a Python3 script.",
            parameters={
                "file": "The absolute file path of the Python3 script that should be executed."
            }
        )
    
    def run(self, file):
        """
        This function will execute the provided Python script.
        """
        try:
            # Execute the script using the subprocess module
            cmd = f"python3 {file}"
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
            # Get the return value of the script
            cmd_return = output.decode('utf-8').strip()
            
            if process.returncode != 0:
                raise Exception(error.decode('utf-8').strip())
            
        except Exception as e:
            return f"An error occurred executing the script: {e}. Please fix the error and try again."
        
        return f"The script was executed successfully. It returned {cmd_return if cmd_return else 'nothing, indicating that you did not achieve your goal.'}"