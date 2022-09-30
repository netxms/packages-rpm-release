# RPM spec for netxms-release package

This package contains spec file and corresponding sources (gpg key, etc.) for the netxms-release package for enterprise linux.

Sources for Server/Agent packages are available at [netxms/packages-rpm](https://github.com/netxms/packages-rpm).

Derived from [epel-release](https://git.rockylinux.org/staging/rpms/epel-release/) package sources.

## Building

```sh
docker build -t netxms-rpm-builder docker
docker run --cap-add=SYS_ADMIN -it --rm  -v $(pwd):/build -v $(pwd)/result:/result netxms-rpm-builder
docker image rm netxms-rpm-builder

# Cache dependencies between builds
#docker run --cap-add=SYS_ADMIN -it --rm -v $(pwd)/cache:/var/cache/mock -v $(pwd):/build -v $(pwd)/result:/result netxms-rpm-builder
```
