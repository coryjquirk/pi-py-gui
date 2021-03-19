from guizero import App, Text, TextBox, PushButton, Slider, Picture, Waffle

app = App(title="truth machine")

welcome_message = Text(app, text="you pick", size=34, font="Helvetica", color="#96b0a3")
my_name = TextBox(app, width=25)

def say_my_name():
    welcome_message.value = my_name.value
update_text = PushButton(app, command=say_my_name, text="say", pady=10)

def change_text_size(slider_value):
    welcome_message.size = slider_value

text_size = Slider(app, command=change_text_size, start=10, end=80)

waffle = Waffle(app, align="bottom", color="#6b8f7d", height=25, width=25, dotty="true")

app.display()
