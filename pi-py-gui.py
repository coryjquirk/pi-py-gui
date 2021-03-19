from guizero import App, Text, TextBox, PushButton, Slider, Picture

app = App(title="truth machine")

welcome_message = Text(app, text="yo check this out", size=34, font="Helvetica", color="#9932CC")
my_name = TextBox(app, width=25)

def say_my_name():
    welcome_message.value = my_name.value
update_text = PushButton(app, command=say_my_name, text="say it to the world")

def change_text_size(slider_value):
    welcome_message.size = slider_value

text_size = Slider(app, command=change_text_size, start=10, end=80)

my_cat = Picture(app, image="green.gif")

app.display()
