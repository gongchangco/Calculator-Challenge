class Calculator:
    def __init__(self):
        self.current_value = ""
        self.parentheses_count = 0
    

    def input(self, value):
        if value == 'C':
            self.clear()
        elif value == '=':
            self.evaluate()
        elif value == '(':
            self.parentheses_count += 1
            self.current_value += value
        elif value == ')':
            if self.parentheses_count > 0:
                self.parentheses_count -= 1
                self.current_value += value
        else:
            self.current_value += value

    def clear(self):
        self.current_value = ""
        self.parentheses_count = 0

    def evaluate(self):
        try:
            # Close any open parentheses
            self.current_value += ')' * self.parentheses_count

            # This is where you'd implement a proper expression evaluator
            # For now, we'll use eval, but this isn't safe for production
            result = eval(self.current_value)
            self.current_value = str(result)
        except Exception as e:
            self.current_value = "Error"
            print(f"Error: {e}")
    
    def get_current_value(self):
        return self.current_value
    
    