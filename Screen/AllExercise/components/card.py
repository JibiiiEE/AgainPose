from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


class Card(MDCard):
    text = StringProperty()
    source = StringProperty()


