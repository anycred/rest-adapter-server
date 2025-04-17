from fastapi import APIRouter

from constants import ASSETS, ACTORS, NEW_ACTOR
from logger import logger
from models import AccessRequestBody, CreateActorRequestBody, DeleteActorRequestBody
from utils.permissions import retrieve_asset_permissions, retrieve_all_permissions

router = APIRouter()

"""It's not necessary to implement all the routes.
Some routes are optional, depending on the mode you choose when setting up the integration.
You can read more in the Entitle documentation.
https://docs.beyondtrust.com/entitle/docs/entitle-integration-rest"""


@router.get('/get_assets')
async def get_assets():
    logger.debug('get_assets called')
    return {'data': {'assets': ASSETS}}


@router.get('/get_actors')
async def get_actors():
    logger.debug('get_actors called')
    return {'data': {'actors': ACTORS}}


@router.get('/get_asset_permissions/{asset_id}')
async def get_asset_permissions(asset_id: str):
    logger.debug(f'get_asset_permissions called with asset_id={asset_id}')
    return {'data': retrieve_asset_permissions(asset_id)}


@router.get('/get_all_permissions')
async def get_all_permissions():
    logger.debug('get_all_permissions called')
    return {'data': retrieve_all_permissions()}


@router.post('/give_access')
async def give_access(data: AccessRequestBody):
    logger.debug(f'give_access called with {data}')
    # Grant access here...
    return {'data': {}}


@router.post('/revoke_access')
async def revoke_access(data: AccessRequestBody):
    logger.debug(f'revoke_access called with {data}')
    # Revoke access here...
    return {'data': {}}


@router.post('/check_config')
async def check_config() -> dict:
    return {
        'data': {
            'valid': True
        }
    }


@router.post('/create_actor')
async def create_actor(data: CreateActorRequestBody) -> dict:
    logger.debug(f'create_actor called with {data}')
    # Create actor here...
    return {
        'next': None,
        'data': {
            'actor': NEW_ACTOR,
            'login_info': {
                'username': 'test'
            }
        }
    }


@router.post('/delete_actor')
async def delete_actor(data: DeleteActorRequestBody) -> dict:
    logger.debug(f'delete_actor called with {data}')
    # Delete actor here...
    return {}
