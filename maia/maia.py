#!/usr/bin/python3

# Prompts
from maia.prompts import *

# Messages
from maia.messages import *

import datetime
import getpass
from groq import Groq
import json
import os
import platform
import re
from termcolor import colored

class MAIA:

    def __init__(self, tools):
        """
        Initialize MAIA.
        """
        if not tools:
            raise ValueError("tools are required")
        
        # Groq Setup
        self.groq_client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        # Tools    
        self.tools = tools

        # System prompt
        self.system_prompt = SYSTEM_PROMPT.format(
            tools=self._get_tools(), 
            tool_names=self._get_tool_names(),
            system_information=self._get_system_information()
        )

        # Inner monologue
        self.inner_monologue = []

        # Colors
        self.user_color = "green"
        self.agent_inner_monologue_color = "light_grey"
        self.agent_response_color = "yellow"

        # Logging
        self.logfile = "./maia.log"
        self.log("M.A.I.A initialized")
    
    def _version(self):
        """
        This function returns the version of M.A.I.A.
        """
        return "v1.0.0"
    
    def _reset(self):
        """
        This function resets M.A.I.A.
        """
        os.system("clear")
        self._welcome()
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ]
    
    def _get_tools(self):
        """
        This function returns the explanations of all available tools.
        """
        return '\n'.join(i.get_tool_explanation() for i in self.tools)
    
    def _get_tool_names(self):
        """
        This function returns the names of all available tools.
        """
        return ', '.join(i.name for i in self.tools)
    
    def _get_system_information(self):
        """
        This function returns some information about the system M.A.I.A is operating on.
        """
        return f"Username: {getpass.getuser()}\nCWD: {os.getcwd()}\nSHELL: {os.environ.get('SHELL')}\nOS: {platform.system()}"
    
    def _save_inner_monologue(self):
        """
        This function saves the inner monologue.
        """
        json.dump(self.inner_monologue, open("./inner_monologue.json", 'w'), indent=4)
    
    def _welcome(self):
        """
        This function prints the welcome message.
        """
        # M.A.I.A
        for i, line in enumerate(WELCOME_MAIA.splitlines()[1:]):
            parts = line.split("|")[1:]
            print(
                colored(parts[0], "green"), 
                colored(parts[1], "magenta"), 
                colored(parts[2], "yellow"), 
                colored(parts[3], "red"), 
            )
        # Credits
        print(WELCOME_CREDITS.format(version=self._version()))
    
    def _color_print(self, message, color):
        """
        This function prints a given message in the specified color.
        """
        print(termcolor.colored(message, color))
    
    def log(self, message):
        """
        This function logs the message to the logfile.
        """
        current_datetime = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M")
        with open(self.logfile, "a") as f:
            f.write(f"[ {current_datetime} ] {message}\n")
    
    def extract_json(self, message):
        """
        This function extracts the JSON content from a given message.
        """
        start_idx = message.find('{')
        end_idx = message.rfind('}')
        
        if start_idx != -1 and end_idx != -1:
            json_str = message[start_idx:end_idx+1]
            try:
                json.loads(json_str)
                return json_str
            except json.JSONDecodeError:
                pass

        self.log(f"JSON Error for content: {message}")
        return '{ "thought": "I did not respond in JSON format.", "action": "Respond", "action-input": {"message": "Internal error occured since I did not respond in propper JSON format. Please ask me to do it again. This time I will do better."} }'

    
    def query_agent(self, message):
        """
        This function queries the agent with a given message.
        """
        # Add user message to conversation
        self.messages.append({"role": "user", "content": message})
        self.log(f"User: {message}")

        # Agent loop
        while True:

            # Query agent
            chat_completion = self.groq_client.chat.completions.create(
                messages=self.messages,
                model="llama3-70b-8192",
                temperature=0
            )
            response_text = chat_completion.choices[0].message.content
            response_json = json.loads(self.extract_json(response_text))

            # Inner Monologue
            self.inner_monologue.append(response_json)
            self._save_inner_monologue()
            self.log(f"Thought: {response_json['thought']}")
            print(f"\n*{colored(response_json['thought'], self.agent_inner_monologue_color)}")

            # Extract action and tool input
            try:
                action, action_input = response_json["action"], response_json["action-input"]
            except:
                action, action_input = "Nothing", "Nothing"
            self.log(f"Action: {action}")
            self.log(f"Input: {action_input}")

            # Respond to human
            if action == "Respond":
                self.messages.append({"role": "assistant", "content": action_input["message"]})
                return action_input["message"]

            # Tool selection
            for t in self.tools:
                if action == t.name:
                    tool = t.run
                    self.log(f"Tool selected: {t.name}")
                    break
            
            # Tool usage
            observation = tool(**action_input)
            self.messages.extend([
                {"role": "assistant", "content": f"Please use the {action} tool to obtain more information."},
                {"role": "user", "content": f"You asked me to use the {action} tool. Here is my observation from it. Please use it and continue your loop.\n\nObservation: {observation}"}
            ])

            # Save conversation
            json.dump(self.messages, open("conversation.json", "w"), indent=4)
    
    def run(self):
        """
        This functino runs MAIA.
        """
        # Welcome message
        self._welcome()

        # Initialize conversation
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ]

        while True:

            # Get user input
            user_input = input(colored("$ ", self.user_color))

            # Exit program
            if user_input == "exit":
                break
                
            # Reset conversation
            if user_input == "clear":
                self._reset()
                continue

            # Query agent
            response = self.query_agent(user_input)

            # Print response
            print(colored(f"\n> {response}\n\n", self.agent_response_color))

            # Save conversation
            json.dump(self.messages, open("conversation.json", "w"), indent=4)