#!/usr/bin/python3

import subprocess

from groq import Groq
import os
from tools import Tool
from tools.pythondeveloper.prompts import *
import uuid


# Python Developer
class PythonDeveloper(Tool):

    def __init__(self):
        """
        Initialize PythonDeveloper.
        """
        # Initialize Tool
        super().__init__(
            name="Python Developer", 
            description="Writes Python code based on your description.",
            usecase="This is useful for when you need to write Python code. You can describe the task and Python Developer will implement it for you.",
            parameters={
                "task": "Your specific task description of what should be implemented. Always start with 'Please implement ...'"
            }
        )

        # Groq Setup
        self.groq_client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        # Initialize messages
        self.messages = self._init_conversation()
        
    def _init_conversation(self):
        """
        Initialize the conversation with Llama-3:instruct.
        """
        return [
            {"role": "system", "content": PYTHON_DEVELOPER},
        ]
    
    def run(self, task):
        """
        This function queries Llama-3:instruct.
        """
        # New conversation
        self.messages = self._init_conversation()
        
        # Add user message
        self.messages.append({"role": "user", "content": task})

        try:
            chat_completion = self.groq_client.chat.completions.create(
                messages=self.messages,
                model="llama3-70b-8192",
                temperature=0,
                max_tokens=1500
            )
            response = chat_completion.choices[0].message.content

            # Write response to random named file
            filename = f"/tmp/{uuid.uuid4()}.py"
            with open(filename, "w") as file:
                file.write(response)

            # Return response
            return f"Python Developer stored the code in a file named {filename}."
        except Exception as e:
            return f"An error occurred executing the command: {e}"