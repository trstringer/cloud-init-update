# Cloud-init Updater

Automatically update cloud-init.

## Installation

`cloud-init-update` is distributed from the `trstringer/cloud-init-update` PPA.

```
# apt-add-repository ppa:trstringer/cloud-init-update
# apt install cloud-init-update
```

*Note*: `cloud-init-update.service` will not run automatically on installation or upgrade. Nor will it run by default. See [Configuration](#configuration) for enabling the updater.

## Configuration

`cloud-init-update` is **disabled by default**. To enable it create a file `/etc/cloud/cloud-init-update.enabled`.

## How it works

The updater is a standalone package and daemon from `cloud-init`. It injects itself into the cloud-init stages by executing after `cloud-init-local.service` and before `cloud-init.service`. This effectively inserts the updater in between the [Local](https://cloudinit.readthedocs.io/en/latest/topics/boot.html#local) service and the [Network](https://cloudinit.readthedocs.io/en/latest/topics/boot.html#network) service.

The logic is simple... the updater will use the package manager (in the case of Ubuntu/Debian, it will use the Python wrapper for apt) to check for any available updates to `cloud-init`. If one exists, then it will install the update. After an update, it will then run `cloud-init clean --logs --reboot`.

## Supported distributions

* Ubuntu
* Debian (untested)

## Supported init systems

Currently only **systemd** is supported.
