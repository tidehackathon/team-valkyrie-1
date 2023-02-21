from pydantic import BaseModel


class TextInput(BaseModel):
    """ A model for input validation """
    text_input: str
