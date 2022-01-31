'''Input Validation class


Attributes
    _validation_options (list): Contains lists of various options
'''
class Input_Validation:
    def __init__(self) -> None:
        self._validation_options = []

    def add_primary(self, primary_input) -> None:
        # Primary inputs are the options that will be returned by the validate method
        self._validation_options.append([primary_input])

    def add_secondary(self, linked_primary, secondary_input) -> None:
        # Secondary inputs are alternite versions of an input that are linked to primary inputs. 
        # Example: "Y" and "Yes" mean the same thing, thus they will return the same option.
        for input_options in self._validation_options:
            if input_options[0] == linked_primary:
                input_options.append(secondary_input)
                return
        
        self._validation_options.append([linked_primary, secondary_input])

    def validate(self, message):
        input_to_validate = input(message)

        for options in self._validation_options:
            for specific_input in options:
                if input_to_validate == specific_input:
                    return options[0]
        
        print("Input not recognized, please try again.")
        return self.validate(message)