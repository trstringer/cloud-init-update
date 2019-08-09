"""Main code path for cloud-init-update."""

import distro
from .apt import check_and_update as apt_check_and_update

def main():
    """Main code execution."""

    linux_distro = distro.linux_distribution()
    if linux_distro[0].lower() in ['ubuntu', 'debian']:
        apt_check_and_update()
    else:
        raise Exception(f'Unknown distro: {linux_distro}')

if __name__ == '__main__':
    main()
