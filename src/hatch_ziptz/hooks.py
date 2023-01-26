from hatchling.plugin import hookimpl
from .plugin import ZiptzBuildHook

@hookimpl
def hatch_register_build_hook():
    return ZiptzBuildHook
