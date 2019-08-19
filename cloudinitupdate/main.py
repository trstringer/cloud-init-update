"""Main code path for cloud-init-update."""

from pathlib import Path
import sys
import distro
from .apt import check_and_update as apt_check_and_update

def _update_is_enabled():
    """
    Determine if cloud-init-update is enabled.

    This currently does the following check(s):
        - Enabled if: /etc/cloud/cloud-init-update.enabled exists.

    The cloud-init updater is disabled by default (in other words, with
    no action, there is no update mechanism) by design. This is currently
    opt-in software.
    """

    return Path('/etc/cloud/cloud-init-update.enabled').exists()

def main():
    """Main code execution."""

    if not _update_is_enabled():
        print('cloud-init-update is disabled')
        sys.exit(0)

    linux_distro = distro.linux_distribution()
    if linux_distro[0].lower() in ['ubuntu', 'debian']:
        apt_check_and_update()
    else:
        print(f'Unknown distro: {linux_distro}')
        sys.exit(1)

if __name__ == '__main__':
    main()
