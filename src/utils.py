from dataclasses import dataclass, field
from typing import Literal, Self

class Buffer:
    def __init__(self):
        self.name = "None"
        self._connect_with = None

    def set_name(self, name):
        self.name = name
        if self._connect_with:
            self._connect_with.name = name

    def connect_with(self, other:"Buffer"):
        self._connect_with = other
        other._connect_with = self

    def __repr__(self) -> str: return f"[{self.name}]"

class Node:
    _inputs_count:int|str = 0
    _outputs_count:int|str = 0
    __nodes__ = []
    def copy_to(self, node:"Node"):
        node._inputs = self._inputs
        node._inputs_count = self._inputs_count
        node._outputs = self._outputs
        node._outputs_count = self._outputs_count
        node.__nodes__ = self.__nodes__

    def __init_subclass__(cls, inputs_count=0, outputs_count=0) -> None:
        cls._inputs_count = inputs_count
        cls._outputs_count = outputs_count

    def __init__(self) -> None:
        self._inputs  = [*map(lambda _: Buffer(), range(self._inputs_count))]
        self._outputs = [*map(lambda _: Buffer(), range(self._outputs_count))]
        self.__nodes__ = [self]

    def __or__(left:"Node", right:"Node") -> "Node":
        ret = Node()
        ret._inputs = [*left._inputs, *right._inputs]
        ret._outputs = [*left._outputs, *right._outputs]
        ret._inputs_count = len(ret._inputs)
        ret._outputs_count = len(ret._outputs)

        ret.__nodes__ = [*left.__nodes__, *right.__nodes__]
        return ret
    
    def __rshift__(left:"Node", right:"Node") -> "Node":
        ret = Node()
        d = right._inputs_count - left._outputs_count
        if d == 0:
            for i in range(abs(right._inputs_count)):
                right._inputs[i].connect_with(left._outputs[i])
            ret._inputs = left._inputs
            ret._outputs = right._outputs
        elif d < 0:
            for i in range(right._inputs_count):
                right._inputs[i].connect_with(left._outputs[i])
            
            ret._inputs = left._inputs
            ret._outputs = [*right._outputs, *left._outputs[d:]]
        elif d > 0:
            for i in range(abs(left._outputs_count)):
                right._inputs[i].connect_with(left._outputs[i])

            ret._inputs = [*left._inputs, *right._inputs[d:]]
            ret._outputs = right._outputs

        ret._inputs_count = len(ret._inputs)
        ret._outputs_count = len(ret._outputs)
        ret.__nodes__ = [*left.__nodes__, *right.__nodes__]
        return ret

    def __repr__(self) -> str:
        input_index = 0
        filter_index = 0

        inputs = [*filter(lambda node: isinstance(node, Input), self.__nodes__)]
        for node in inputs:
            for out in node._outputs:
                out.set_name(f"{input_index}")
                input_index += 1

        filters = [*filter(lambda node: isinstance(node, Filter), self.__nodes__)]
        for node in filters:
            for out in node._outputs:
                out.set_name(f"f{filter_index}")
                filter_index += 1

        outputs = [*filter(lambda node: isinstance(node, Output), self.__nodes__)]

        inputs_txt = ' '.join(map(str, inputs))
        filters_txt = ""
        if filters:
            filters_txt = '; '.join(map(str, filters))
            filters_txt = f" -filter_complex \"{filters_txt}\""
        
        outputs_txt = ' '.join(map(str, outputs))
        return f"ffmpeg {inputs_txt} "\
               f" {filters_txt} "\
               f" {outputs_txt}"
      
class GlobalOptions(Node):
    def __init__(self, loglevel, report, max_alloc, bytes, ignore_unknown, filter_threads, filter_complex_threads, stats, max_error_rate, hide_banner) -> None:
        super().__init__()

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
        if self._inputs[0]._connect_with:
            txt += f" -map '{self._inputs[0]}' "

        if self.frames != -1:
            txt += f" -frames {self.frames} "

        if self.overwrite == "yes":
            txt += " -y "
        elif self.overwrite == "no":
            txt += " -n "

        return f" {txt} {self.output} "


class Filter(Node):
    _next_filters = []
    name = ""
    def __post_init__(self) -> None:
        Filter.__init__(self)
        #before = set(self.__dict__)
        #if "__next_filters__" in self.__dir__():
        #    self.__next_filters__()
        #after = set(self.__dict__)
        #self._next_filters = [*(after - before)]
        self.__filters__ = [self]

    def __getattribute__(self, __name: str) -> "Filter":
        attr = object.__getattribute__(self, __name)
        #_next_filters = object.__getattribute__(self, "_next_filters")
        #if __name in _next_filters:
        #    _right_filter = attr            
        #    is_in_filters = [*filter(lambda f: __name == f.__class__.__name__, 
        #                             object.__getattribute__(self, "__nodes__"))]
        #    if is_in_filters:
        #        return is_in_filters[-1]
        #    return lambda *args, **kwds: Filter.__rshift__(self, _right_filter(*args, **kwds))
        
        if __name in ["_inputs_count", "_outputs_count"]:
            try:
                return int(attr)
            except:
                return object.__getattribute__(self, attr)
        return attr
    
    #def __call__(self, *args, **kwds):
    #    Filter.__rshift__(self, type(self)(*args, **kwds))

    def __repr__(self) -> str:
        def _map(f):
            opt_name = f.name
            if f.metadata:
                opt_name = f.metadata
            return f"{opt_name}={self.__getattribute__(f.name)}"
        opts =  [*
                # Convert the filtered variables to a string like "filter_name=[opt_name=opt_val:opt_name=opt_val:...]"
                map(_map,
                    # Filter different variables from the default value 
                    filter(lambda f: f.default != self.__getattribute__(f.name), 
                            self.__dataclass_fields__.values()))]
        _str = self.__class__.__name__.lower()
        if self.name:
            _str += f"@{self.name}"
            
        if opts:
            _str += "=" + ':'.join(opts)
        return ''.join(map(str, self._inputs)) + _str + ''.join(map(str, self._outputs))