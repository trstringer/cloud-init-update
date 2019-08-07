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

    ci_pkg_is_upgradable = _ci_pkg_is_upgradable()

    if ci_pkg_is_upgradable is None:
        raise Exception(f'{_CLOUD_INIT_PKG_NAME} not found')

    if ci_pkg_is_upgradable:
        print(f'{_CLOUD_INIT_PKG_NAME} is upgradable')
    else:
        print(f'{_CLOUD_INIT_PKG_NAME} is not upgradable')

def _ci_pkg_is_upgradable():
    """
    Get the installed cloud-init package version.

    Args:
        None

    Returns:
        str: Package version of installed cloud-init.
    """

    apt.Cache().update()

    for pkg in apt.Cache():
        if pkg.shortname == _CLOUD_INIT_PKG_NAME:
            return pkg.is_upgradable

    # This is unexpected, but in the event that cloud-init is not
    # installed on the machine we should return nothing.
    return None
