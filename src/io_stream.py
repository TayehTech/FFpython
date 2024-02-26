from typing import Literal
from .node import Node

class Input(Node, outputs_count=1):
    def __init__(self, input:str=None, format:str=None, loop=0) -> None:
        self.input = input
        self.format = format
        self.loop = loop
        super().__init__()

    def __repr__(self):
        txt = ""
        if self.format:
            txt += f" -f {self.format} "
        if self.loop:
            txt += f" -loop {self.loop} "
        return f" {txt} -i {self.input} "

class Output(Node, inputs_count=1):
    def __init__(self, output="", overwrite:Literal["yes", "no", "ask"]="ask", frames=-1) -> None:
        self.frames = frames
        self.overwrite = overwrite
        self.output = output
        super().__init__()

    def __repr__(self) -> str:
        txt = ""
        if self.inputs[0]._connect_with:
            txt += f" -map '{self.inputs[0]}' "

        if self.frames != -1:
            txt += f" -frames {self.frames} "

        if self.overwrite == "yes":
            txt += " -y "
        elif self.overwrite == "no":
            txt += " -n "

        return f" {txt} {self.output} "