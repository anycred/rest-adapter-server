"""
This module represents the mock data for our rest integration server.
It represents the following scenario:
    - Three accounts - John, Jane and Hugh
    - Three groups
        - An account may be a member, admin or owner (or nothing)
    - One repository
        - An account may be a maintainer or an admin (or nothing)
    - Several permissions are specified. Let's focus on the repository (asset id '3'):
        - John is a maintainer (ACTOR_PERMISSIONS)
        - Having any permission to asset '4' ("Admins" group) grants 'admin' permissions on the repo (ASSET_PERMISSIONS)
        - Jane is a member in asset '4' and therefore has 'admin' permissions on the repo
"""

GROUP_ROLE_OPTIONS = [
    {'code': 'member', 'display_name': 'Member'},
    {'code': 'admin', 'display_name': 'Admin'},
    {'code': 'owner', 'display_name': 'Owner'},
]

REPO_ROLE_OPTIONS = [
    {'code': 'maintainer', 'display_name': 'Maintainer'},
    {'code': 'admin', 'display_name': 'Admin'},
]

ASSETS = [
    {'identifier': '1', 'name': 'First Group', 'type': 'group', 'role_options': GROUP_ROLE_OPTIONS},
    {'identifier': '2', 'name': 'Second Group', 'type': 'group', 'role_options': GROUP_ROLE_OPTIONS},
    {'identifier': '3', 'name': 'Best Repo Ever', 'type': 'repo', 'role_options': REPO_ROLE_OPTIONS},
    {'identifier': '4', 'name': 'Admins', 'type': 'group', 'role_options': GROUP_ROLE_OPTIONS}
]

ACTORS = [
    {'identifier': 'john_doe', 'name': 'John Doe', 'type': 'user', 'email': 'john_doe@gmail.com'},
    {'identifier': 'jane_doe', 'name': 'Jane Doe', 'type': 'user', 'email': 'jane_doe@gmail.com'},
    {'identifier': 'hugh', 'name': 'Hugh Jackman', 'type': 'user', 'email': 'hugh@gmail.com'},
]

ACTOR_PERMISSIONS = {  # by asset identifier
    '1': [
        {'actor_id': 'john_doe', 'role_code': 'member'},
        {'actor_id': 'hugh', 'role_code': 'admin'},
    ],
    '2': [
        {'actor_id': 'john_doe', 'role_code': 'member'},
        {'actor_id': 'jane_doe', 'role_code': 'owner'},
    ],
    '3': [
        {'actor_id': 'john_doe', 'role_code': 'maintainer'},
    ],
    '4': [
        {'actor_id': 'jane_doe', 'role_code': 'member'},
    ]
}

ASSET_PERMISSIONS = {  # by asset identifier
    '3': [
        {'asset_id': '4', 'role_code': 'admin'},
    ]
}
