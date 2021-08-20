name = "shellServer"
version = "0.0.0"

variants = [
    ["python-2"],
    ["python-3"]
]

requires = [
    "python",
]

tools = [
    "server"
]

def commands():
    env.PATH.append("{root}/src")
    env.PYTHONPATH.append("{root}/src")
 