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
            description="Saves any Python3 script to disk and executes it.",
            usecase="This is useful for when you decide to write and execute some Python3 code to solve a given problem. The script must always return a string such that you can further work with it. ",
            parameters={
                "name": "The name of the Python3 script.",
                "content": "The Python3 script that should be executed. This must include all needed imports."
            }
        )
    
    def run(self, name, content):
        """
        This function will execute the provided Python script.
        """
        try:
            # Save the script to a temporary file
            script_path = f"/tmp/{name}.py"
            with open(script_path, "w") as file:
                file.write(content)
            
            # Execute the script using the subprocess module
            cmd = f"python3 {script_path}"
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
            # Get the return value of the script
            cmd_return = output.decode('utf-8').strip()
            
            if process.returncode != 0:
                raise Exception(error.decode('utf-8').strip())
            
        except Exception as e:
            return f"An error occurred executing the command: {e}"
        
        return f"The script was executed successfully. It returned {cmd_return if cmd_return else 'nothing, indicating that you did not achieve your goal.'}"