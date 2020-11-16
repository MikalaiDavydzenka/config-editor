from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

buffer1 = Buffer()  # Editable buffer.

kb = KeyBindings()


@kb.add('q')
def exit_(event):
    event.app.exit()


root_container = VSplit([
    # One window that holds the BufferControl with the default buffer on
    # the left.
    Window(content=BufferControl(buffer=buffer1)),

    # A vertical line in the middle. We explicitly specify the width, to
    # make sure that the layout engine will not try to divide the whole
    # width by three for all these windows. The window will simply fill its
    # content by repeating this character.
    Window(width=1, char='|'),

    # Display the text 'Hello world' on the right.
    Window(content=FormattedTextControl(text='Hello world')),
])

layout = Layout(root_container)

app = Application(
    layout=layout,
    key_bindings=kb,
    full_screen=True,
)
app.run() # You won't be able to Exit this app