#!/usr/bin/python3

# Parent class for all tools
class Tool:

    def __init__(self, name, description, usecase, parameters):
        """
        Initialize Tool.
        """
        if not name:
            raise ValueError("name is required")
        if not description:
            raise ValueError("description is required")
        if not usecase:
            raise ValueError("usecase is required")
        if not parameters:
            raise ValueError("parameters are required")
        
        self.name = name
        self.description = description
        self.usecase = usecase
        self.parameters = parameters

    def run(self):
        """
        This function runs the tool and returns a result.
        """
        raise NotImplementedError("Subclasses must implement run method")

    def __str__(self):
        """
        This function is used to print out the name of the tool.
        """
        return f"{self.name} Tool"
    
    def get_tool_explanation(self):
        """
        This function returns a string explaining how to use this tool.
        """
        return f"{self.name}: {self.description} {self.usecase} The following parameters are necessary: {self.parameters}"