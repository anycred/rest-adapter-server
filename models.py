from pydantic import BaseModel


class AccessRequestBody(BaseModel):
    asset: dict
    actor_identifier: str
    role_code: str
