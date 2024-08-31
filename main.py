import os
import importlib

from kivy.core.window import  Window

from kaki.app import App
from kivymd.app import MDApp

class AgainPoseLive(App, MDApp):
    KV_FILES = {
        os.path.join(
            os.getcwd(), "Screen", "AllExercise", "all_exercise.kv"
        ),
        os.path.join(
            os.getcwd(), "Screen", "AllExercise", "components", "card.kv"
        ),
        os.path.join(
            os.getcwd(), "Screen", "RootScreen", "root_screen.kv"
        ),
        os.path.join(
            os.getcwd(), "Screen", "TodayScreen", "today_screen.kv"
        ),
    }

    CLASSES = {
        "AllExercise": "Screen.AllExercise.all_exercise",
        "Card": "Screen.AllExercise.components.card",
        "RootScreen": "Screen.RootScreen.root_screen",
        "TodayScreen": "Screen.TodayScreen.today_screen",
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]

    def on_card_release(self, card_text):
        print(f"Card with text '{card_text} was clicked!")

    def build_app(self):
        self.theme_cls.primary_palette = "Amber"
        import Screen.RootScreen.root_screen

        Window.bind(on_keyboard=self.rebuild)
        importlib.reload(Screen.RootScreen.root_screen)

        return Screen.RootScreen.root_screen.RootScreen()

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()

AgainPoseLive().run()