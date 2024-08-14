from constants import ACTOR_PERMISSIONS, ASSET_PERMISSIONS, ASSETS


def retrieve_asset_permissions(asset_id: str) -> dict:
    return {
        'actors_permissions': ACTOR_PERMISSIONS.get(asset_id, []),
        'assets_permissions': ASSET_PERMISSIONS.get(asset_id, [])
    }


def retrieve_all_permissions() -> dict:
    return {
        'actors_permissions': {asset['identifier']: ACTOR_PERMISSIONS.get(asset['identifier'], []) for asset in ASSETS},
        'assets_permissions': {asset['identifier']: ASSET_PERMISSIONS.get(asset['identifier'], []) for asset in ASSETS},
    }
