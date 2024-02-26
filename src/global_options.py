from dataclasses import dataclass
from typing import Literal
from .node import Node

LOG_LEVELS = Literal[
    'repeat',
    'level',
    'quiet',   '-8',
    'panic',   '0',
    'fatal',   '8',
    'error',   '16',
    'warning', '24',
    'info',    '32',
    'verbose', '40',
    'debug',   '48',
    'trace',   '56']

CPU_FLAGS = Literal[
    'armv5te',
    'armv6',
    'armv6t2',
    'vfp',
    'vfpv3',
    'neon',
    'setend']

ABORT_ON_FLAGS = Literal[
    "empty_output",
    "empty_output_stream"
]

@dataclass(repr=False, eq=False) 
class GlobalOptions(Node):
    loglevel:LOG_LEVELS = None
    hide_banner:bool = False
    report:bool = False
    stats:bool = False
    cpuflags:CPU_FLAGS = None
    cpucount:int = None
    benchmark:bool = False
    benchmark_all:bool = False
    max_error_rate:float = "2/3"
    
    max_alloc:bytes = None
    ignore_unknown:bool = False
    nostats:bool = False
    recast_media:bool = False
    debug_ts:bool = False
    dump:bool = False
    hex:bool = False
    xerror:bool = False
    auto_conversion_filters:bool = False

    timelimit:float = None
    max_alloc:int = None
    filter_threads:int = None
    stats_period:str = None
    progress:str = None
    vsync:str = None
    filter_complex_threads:int = None
    sdp_file:str = None
    abort_on:ABORT_ON_FLAGS = None

    v:LOG_LEVELS = None

    _fields_without_args = [
        "hide_banner",
        "report",
        "ignore_unknown",
        "stats",
        "recast_media",
        "nostats",
        "debug_ts",
        "benchmark",
        "benchmark_all",
        "dump",
        "hex",
        #"max_error_rate",
        "xerror",
        "auto_conversion_filters"
    ]

    def __post_init__(self) -> None:
        super().__init__()
    
    def __repr__(self) -> str:
        def _remap(field):
            if field.name in self._fields_without_args:
                if self.__getattribute__(field.name):
                    return f"-{field.name}"
                else:
                    return ""
                
            return f"-{field.name} {self.__getattribute__(field.name)}"
        opts =  [*
                 # remap to -opt_name opt_val
                map(_remap,
                    filter(lambda f: f.default != self.__getattribute__(f.name), 
                            self.__dataclass_fields__.values()))]
        
        return " ".join(opts)
