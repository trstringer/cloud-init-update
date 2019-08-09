"""Update code path for Ubuntu."""

import subprocess
import apt

_CLOUD_INIT_PKG_NAME = 'cloud-init'

def check_and_update():
    """
    Update cloud-init.

    Args:
        None

    Returns:
        None
    """

    cache = apt.Cache()
    cache.update()

    if not cache[_CLOUD_INIT_PKG_NAME].is_installed:
        raise Exception(f'{_CLOUD_INIT_PKG_NAME} is not installed')

    if cache[_CLOUD_INIT_PKG_NAME].is_upgradable:
        print(f'{_CLOUD_INIT_PKG_NAME} is upgradable. Upgrading...')
        cache[_CLOUD_INIT_PKG_NAME].mark_upgrade()
        cache.commit()
        subprocess.run(['cloud-init', 'clean', '--logs', '--reboot'])
    else:
        print(f'{_CLOUD_INIT_PKG_NAME} is not upgradable')
