import http.server
import os

folder = os.path.join(os.path.dirname(__file__), "page")

os.makedirs(folder, exist_ok=True)


class HTML:
  template = "<p>{}</p>"
  def __init__(self, *content: str):
    content = [c.render() if isinstance(c, HTML) else c for c in content]
    self.content = "\n".join(content).strip().split("\n")

  def render(self): return self.template.format("\n".join(self.content))

class h(HTML):
  template = "<h{}>{{}}</h{}>"
  def __init__(self, content:str, n:int):
    super().__init__(content)
    self.template = self.template.format(n,n)

class p(HTML): template = "<p>{}</p>"
class Output(HTML): template = "<pre style='color:#8f8;padding:0; padding-left:10px;'>{}</pre>"

class CodeBlock(HTML):
  template = '''<pre style="background-color: #333;padding: 10px;border-radius: 5px;"><code>{}</code></pre>'''
  def __init__(self, *content: str):
    self.output = []
    self.content = "\n".join(content).strip().split("\n")
    
  def render(self): 
    lines = [f'<span style="color:#8af;"><span style="color: #555; padding-right: 10px;">{i+1}</span> {l} </span>' for i, l in enumerate(self.content)]
    code = self.template.format("\n".join(lines))
    if self.output: code += Output(*self.output).render()
    return code


class Section(HTML):
  def __init__(self, title: str, *blocks: HTML):
    self.title = title
    self.blocks = [HTML(b) if isinstance(b, str) else b for b in blocks]
    codeblocks = [b for b in blocks if isinstance(b, CodeBlock)]
    output = []

    def _print(*args):
      nonlocal output
      output.append(" ".join(str(a) for a in args) + "\n")
    def reset_output():
      nonlocal output
      output = []
    code = ""
    for b in codeblocks:
      code += "\nreset()\n" + "\n".join(b.content) + "\n"
      exec(code, {"print": _print, "reset": reset_output})
      if output: b.output = output
      output = []
    
    
    super().__init__(h(title, 2), *self.blocks)


try:
  content = HTML(
    Section("Hello World",
      p("the simplest python program creates a single line of output:"),
      CodeBlock("print('Hello World')"),
      "The green text under the code is the output of the program.",
      "print is used to output text to the console.",
    ),
    Section("Variables",
      p("Variables are used to store data."),
      CodeBlock("x = 10"),
      CodeBlock("y = 20"),
      CodeBlock("z = x + y"),
      CodeBlock("print(z)"),
    ),
    Section("Functions",
      "Functions are maybe the most important concept in programming.",
      "used to package commands into a single name",
      "a math function f(x) = x + 1 looks like this in python:",
      CodeBlock(
        "def f(x):",
        "  return x + 1"),
      "the return statement ends the function and returns the value to the caller.",
      CodeBlock("print(f(10))","print(f(20))"),
      "this is how we call a function with the argument 10 and 20.",
      CodeBlock(
        "def g(x):",
        "  a = 22 + x",
        "  return x * a",
        "",
        "print(g(10))"
        ),
      "A function can have multiple lines.",
      "Identation defines what is inside the function.",
      CodeBlock(
        "def add(x, y):",
        "  a = x + y",
        "  b = g(a)",
        "  return a, b",
        "",
        "print(add(10, 20))",
        ),
      "This function takes two arguments, calls another function and then returns two values.",
        
    )
  )

except Exception as e:
  content = HTML(
    p(f"Error: {e}")
  )


  with open(folder+"/index.html", "w") as f:
    f.write(f"""
    <html>
    <body>
    {content.render()}
    <script>
    </script>
    <style>
    body {{
      background-color: #000;
      color: #fff;
      padding: 5% 10%;
      font-family: apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    }}
    </style>
    </body>
    </html>
    """)

    raise e



with open(folder+"/index.html", "w") as f:
  f.write(f"""
  <html>
  <body>
  {content.render()}
  <script>
  </script>
  <style>
  body {{
    background-color: #000;
    color: #fff;
    padding: 5% 10%;
    font-family: apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  }}
  </style>
  </body>
  </html>
  """)
