from abc import ABC

# Import ABC


class Writer:

    def __init__(self,name):
        self.name=name
        self.__tools=None

    @property
    def tools(self):
        return self.__tools

    @tools.setter
    def tools(self, tool):
        self.__tools=tool


class Tool(ABC):

    def __init__(self, name):
        self.name=name




    def message(self):
        return f"I am using the tool {self.name}"


class Pen(Tool):
    def __init__(self, name="Pen"):
        super().__init__(name)

class TypeWriter(Tool):

    def __init__(self, name="TypeWriter"):
        super().__init__(name)



if __name__ == '__main__':

    tp=Pen()
    tpw=TypeWriter()
    writer=Writer("Peter")
    writer.tools=tpw
    print(dir())
    print(writer.tools.message())