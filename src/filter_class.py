from node import Node

class Filter(Node):
    _next_filters = []
    name = ""
    def __post_init__(self) -> None:
        Filter.__init__(self)

    def __getattribute__(self, __name: str) -> "Filter":
        attr = object.__getattribute__(self, __name)
        if __name in ["inputs_count", "outputs_count"]:
            try:
                return int(attr)
            except:
                return object.__getattribute__(self, attr)
        return attr

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
        return ''.join(map(str, self.inputs)) + _str + ''.join(map(str, self.outputs))
    