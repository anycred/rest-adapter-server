from pydantic import BaseModel


class AccessRequestBody(BaseModel):
    asset: dict
    actor_identifier: str
    role_code: str

class CreateActorRequestBody(BaseModel):
    asset: dict
    provisioning_data: dict
    role_code: str

class DeleteActorRequestBody(BaseModel):
        asset: dict
        actor_identifier: str

