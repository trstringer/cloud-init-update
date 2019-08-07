"""Update code path for Ubuntu."""

import apt

_CLOUD_INIT_PKG_NAME = 'cloud-init'

def check_and_update():
    """
    Main entrypoint for Ubuntu updating.

    Args:
        None

    Returns:
        None
    """

    cache = apt.Cache()
    cache.update()

    if cache[_CLOUD_INIT_PKG_NAME].is_upgradable:
        print(f'{_CLOUD_INIT_PKG_NAME} is upgradable. Upgrading...')
        cache[_CLOUD_INIT_PKG_NAME].mark_upgrade()
        cache.commit()
    else:
        print(f'{_CLOUD_INIT_PKG_NAME} is not upgradable')
