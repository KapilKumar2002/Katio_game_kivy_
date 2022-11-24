from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton
from modules.level1 import Level1
from modules.level2 import Level2

class Screens(ScreenManager):
    pass


class CGgameApp(MDApp):
    dialog = None
    def build(self):
        self.load_all_kv_files()
        return Screens()
    
    def load_all_kv_files(self):
        Builder.load_file("homepage.kv")
        Builder.load_file("modules/level1.kv")
        Builder.load_file("modules/level2.kv")
        Builder.load_file("screens.kv")
    def get_home(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Settings",
                text= "Are you sure?",
                auto_dismiss = False,
                buttons=[
                MDFillRoundFlatIconButton(icon = "exit-to-app", text='Quit',on_release=self.home), 
                MDFillRoundFlatIconButton(icon = "play", text='Play',on_release=self.dialog_close), 
                ]
            )
        self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)
    def home(self, *args):
        MDApp.get_running_app().root.current = "home"


if __name__ == "__main__":
    LabelBase.register(name="lcd", fn_regular="font/Lcd.ttf")
    LabelBase.register(name="SBpoppins", fn_regular="font/Poppins SemiBold 600.ttf")
    LabelBase.register(name="Bpoppins", fn_regular="font/Poppins Bold 700.ttf")
    CGgameApp().run()
