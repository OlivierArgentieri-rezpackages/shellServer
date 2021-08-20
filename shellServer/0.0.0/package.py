name = "shellServer"
version = "0.0.0"

requires = [
    "python",
]

tools = [
    "server"
]

def commands():
    env.PATH.append("{root}/src")
    env.PYTHONPATH.append("{root}/src")
 