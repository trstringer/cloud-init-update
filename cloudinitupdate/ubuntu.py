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

    apt.Cache().update()

    ci_pkg = [
        pkg
        for pkg
        in apt.Cache()
        if pkg.shortname == _CLOUD_INIT_PKG_NAME
    ]
    if not ci_pkg:
        raise Exception(f'{_CLOUD_INIT_PKG_NAME} not found')

    if ci_pkg.is_upgradable:
        print(f'{_CLOUD_INIT_PKG_NAME} is upgradable. Upgrading...')
        ci_pkg.mark_upgrade()
    else:
        print(f'{_CLOUD_INIT_PKG_NAME} is not upgradable')
