def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - env: the mkdocs-macros environment, whose `variables` dict holds page
      variables and whose `macro` decorator registers a Jinja2 callable.
    """

    @env.macro
    def inputcode(filename, language, startline=0, endline=None):
        filename = '../' + filename  # file path must be given relative to root directory
        f = open(filename, 'r')
        if startline != 0 or endline != None:
            lines = f.readlines()
            lines = lines[startline:endline]
            text = "".join(lines)
        else:
            text = f.read()
        textblock = f'```{language}\n{text}\n```'
        return textblock

    @env.macro
    def inputcpp(filename, startline=0, endline=None):
        return inputcode(filename, 'cpp', startline, endline)
