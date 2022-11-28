from abc import ABC, abstractmethod


class Command(ABC): 
    """The Command interface declares a method for executing a command."""
    @abstractmethod
    def execute(self, param):
        pass


class Task(Command):
    """Some commands can implement simple operations on their own."""
    def __init__(self):
        self.list = []

    def add(self, task: Command):
        self.list.append(task)

    def execute(self, param):
        for task in self.list:
            task.execute(param)