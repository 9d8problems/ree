import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class DiceGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.points = 100
        self.create_ui()

    def create_ui(self):
        self.label = Label(text=f"Current points: {self.points}")
        self.add_widget(self.label)

        self.wager_input = TextInput(hint_text="Enter your wager", multiline=False, size_hint=(None, None), size=(150, 50))
        self.add_widget(self.wager_input)

        self.over_button = Button(text="Over", size_hint=(None, None), size=(150, 50), on_press=self.play_game)
        self.add_widget(self.over_button)

        self.under_button = Button(text="Under", size_hint=(None, None), size=(150, 50), on_press=self.play_game)
        self.add_widget(self.under_button)

        self.result_label = Label()
        self.add_widget(self.result_label)

    def play_game(self, instance):
        wager = int(self.wager_input.text) if self.wager_input.text.isdigit() else 0
        guess = instance.text.lower()

        if not 1 <= wager <= self.points:
            self.result_label.text = "Invalid wager. Please enter a valid amount."
            return

        roll = random.randint(1, 100)
        self.result_label.text = f"Roll result: {roll}"

        if (guess == 'over' and roll > 50) or (guess == 'under' and roll <= 50):
            self.result_label.text += "\nYou guessed correctly!"
            self.points += wager
        else:
            self.result_label.text += "\nSorry, you guessed incorrectly."
            self.points -= wager

        self.label.text = f"Current points: {self.points}"
        self.wager_input.text = ""
        self.result_label.text += "\nDo you want to play again?"

        if self.points <= 0:
            self.over_button.disabled = True
            self.under_button.disabled = True
            self.result_label.text += "\nGame over. Thanks for playing!"

    def reset_game(self):
        self.points = 100
        self.label.text = f"Current points: {self.points}"
        self.over_button.disabled = False
        self.under_button.disabled = False
        self.result_label.text = ""

    def update_ui(self):
        self.clear_widgets()
        self.create_ui()


class DiceGameApp(App):
    def build(self):
        return DiceGame()


if __name__ == "__main__":
    DiceGameApp().run()
