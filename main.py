from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from calculator import Calculator

class CalculatorApp(App):
    def build(self):
        self.calculator = Calculator()
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )

        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["(", ")"]
        ]

        for row in buttons:
            h_layout = BoxLayout()

            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            
            main_layout.add_widget(h_layout)
        
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        equals_button.bind(on_press=self.on_button_press)
        main_layout.add_widget(equals_button)

        return main_layout
    
    def on_button_press(self, instance):
        button_text = instance.text
        self.calculator.input(button_text)
        self.solution.text = self.calculator.get_current_value()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()