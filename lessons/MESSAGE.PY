"""Class to store a message."""

class Email:

    to: str
    message: str
    important: bool

    def __init__(self, recipiant: str, message_text:str, important_flag: bool):
        """Going to define a function."""
        self.to = recipiant
        self.message = message_text
        self.important = important_flag
    
    
    def __str__(self) -> str:
        """rahh"""   
        m_string: str = f"To: {self.to} \n "
        m_string += f"Important? {self.important}\n"
        m_string += f"{self.message}"
        return m_string
    

    def __mul__(self, factor: int):
        self.message *= factor


email_to_chiara: Email = Email("chiara", "You are a great TA", False)
email_to_chiara * 100
print(email_to_chiara)