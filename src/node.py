class Buffer:
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, __name) -> str:
        self.__name = __name
        if self._connect_with:
            self._connect_with.__name = __name

    def __init__(self):
        self.__name = "None"
        self._connect_with = None
    

    def connect(self, other:"Buffer"):
        self._connect_with = other
        other._connect_with = self

    def __repr__(self) -> str: return f"[{self.name}]"

class Node(object):
    inputs_count:int|str = 0
    outputs_count:int|str = 0
    __nodes__:list["Node"] = []

    def copy_to(self, node:"Node"):
        node.inputs = self.inputs
        node.inputs_count = self.inputs_count
        node.outputs = self.outputs
        node.outputs_count = self.outputs_count
        node.__nodes__ = self.__nodes__

    def __init_subclass__(cls, inputs_count=0, outputs_count=0) -> None:
        cls.inputs_count = inputs_count
        cls.outputs_count = outputs_count

    def __init__(self) -> None:
        self.inputs  = [*map(lambda _: Buffer(), range(self.inputs_count))]
        self.outputs = [*map(lambda _: Buffer(), range(self.outputs_count))]
        self.__nodes__ = [self]

    def __or__(left:"Node", right:"Node") -> "Node":
        ret = Node()
        ret.inputs = [*left.inputs, *right.inputs]
        ret.outputs = [*left.outputs, *right.outputs]
        ret.inputs_count = len(ret.inputs)
        ret.outputs_count = len(ret.outputs)

        ret.__nodes__ = [*left.__nodes__, *right.__nodes__]
        return ret
    
    def __rshift__(left:"Node", right:"Node") -> "Node":
        ret = Node()
        d = right.inputs_count - left.outputs_count
        if d == 0:
            for i in range(abs(right.inputs_count)):
                right.inputs[i].connect(left.outputs[i])
            ret.inputs = left.inputs
            ret.outputs = right.outputs
        elif d < 0:
            for i in range(right.inputs_count):
                right.inputs[i].connect(left.outputs[i])
            
            ret.inputs = left.inputs
            ret.outputs = [*right.outputs, *left.outputs[d:]]
        elif d > 0:
            for i in range(abs(left.outputs_count)):
                right.inputs[i].connect(left.outputs[i])

            ret.inputs = [*left.inputs, *right.inputs[d:]]
            ret.outputs = right.outputs

        ret.inputs_count = len(ret.inputs)
        ret.outputs_count = len(ret.outputs)
        ret.__nodes__ = [*left.__nodes__, *right.__nodes__]
        return ret

    def __repr__(self) -> str:
        from .global_options import GlobalOptions
        from .filter_class import Filter
        from .io_stream import Input, Output

        g_opts  = [*filter(lambda node: isinstance(node, GlobalOptions), self.__nodes__)]
        inputs  = [*filter(lambda node: isinstance(node,    Input     ), self.__nodes__)]
        filters = [*filter(lambda node: isinstance(node,    Filter    ), self.__nodes__)]
        outputs = [*filter(lambda node: isinstance(node,    Output    ), self.__nodes__)]
        
        for i, node in enumerate(inputs):
            for out in node.outputs:
                out.name = f"{i}"

        for i, node in enumerate(filters):
            for out in node.outputs:
                out.name = f"f{i}"

        g_opts_txt = ' '.join(map(str, g_opts))

        inputs_txt = ' '.join(map(str, inputs))

        filters_txt = ""
        if filters:
            filters_txt = f" -filter_complex \"" + '; '.join(map(str, filters)) + "\""
        
        outputs_txt = ' '.join(map(str, outputs))
        
        return f"ffmpeg {g_opts_txt} {inputs_txt} "\
               f" {filters_txt} "\
               f" {outputs_txt}"
