from kivy.app import App
from kivy.uix.label import Label


class FrmPrincipal(App):
    def build(self):
        label = Label(text='a')
        return Label
       
app = FrmPrincipal()
app.run()



