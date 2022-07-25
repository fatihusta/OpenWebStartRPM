# Convert OpenWebStart deb package to rpm
This project just converting prebuilded deb package to rpm package.
```
git clone --depth 1 https://github.com/fatihusta/OpenWebStartRPM.git
```
```
cd OpenWebStartRPM
```
I used fedora 36. Probably works all rpm based distro.
```
export OWS_VERSION=1.6.0
export RPM_RELEASE=1  # Optional, default is 1
docker run \
       --rm \
       --workdir /root/ows \
       --volume $(pwd):/root/ows \
       fedora:36 \
       /bin/sh /root/ows/build.sh $OWS_VERSION $RPM_RELEASE
```
When build finished rpm will be in your host system. **RPM output is your current directory on your host machine**
Ex: OpenWebStart-1.6.0-1.fc36.x86_64.rpm

You can install package via dnf or yum with dependencies.
```
sudo dnf install OpenWebStart-1.6.0-1.fc36.x86_64.rpm
```

