from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class VendasWindows(BoxLayout):
    def _init_(self, **kwargs):
       super()._init_(**kwargs)


class VendasApp(App):
    def build(self):
        return VendasWindows()
 
if __name__ == '__main__':
    VendasApp().run()
