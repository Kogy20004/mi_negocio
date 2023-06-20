from reactpy import component, html
from reactpy.backend.starlette import configure


@component
def HelloWorld():
    return html.h1("Hello, world!")


app = Starlette()
configure(app, HelloWorld)