from pydantic import BaseModel

class EchoModel(BaseModel):
    user_input: str
    query_type: str
    len_chars: int