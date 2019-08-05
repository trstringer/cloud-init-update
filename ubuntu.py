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

    installed_ci_version = _installed_ci_pkg_version()

    if not installed_ci_version:
        raise Exception(f'{_CLOUD_INIT_PKG_NAME} not found')

    print(f'Current {_CLOUD_INIT_PKG_NAME} package version is {installed_ci_version}')

def _installed_ci_pkg_version():
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
            for pkg_version_key in pkg.versions.keys():
                pkg_version = pkg.versions.get(pkg_version_key)
                if pkg_version.is_installed:
                    return pkg_version.version

    # This is unexpected, but in the event that cloud-init is not
    # installed on the machine we should return nothing.
    return None
