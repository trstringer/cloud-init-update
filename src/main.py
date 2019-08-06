"""Main code path for cloud-init-update."""

import argparse
from .ubuntu import check_and_update

def main():
    """Main code execution."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d', '--distro',
        help='Current distribution',
        default='ubuntu'
    )

    args = parser.parse_args()

    print(f'Distro: {args.distro}')

    if args.distro.lower() == 'ubuntu':
        check_and_update()

if __name__ == '__main__':
    main()
