from fastapi import APIRouter

from constants import ASSETS, ACTORS
from logger import logger
from models import AccessRequestBody
from utils.permissions import retrieve_asset_permissions, retrieve_all_permissions

router = APIRouter()


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
