#!/bin/sh
# Author: Fatih Usta <fatihusta86@gmail.com>
# License: MIT

OWS_VER=${1:-'1.6.0'}
OWS_REL=${2:-'1'}
OWS="https://github.com/karakun/OpenWebStart/releases/download/v$OWS_VER/OpenWebStart_linux_${OWS_VER//\./_}.deb"

# Install requierments
dnf install -y \
	rpm-build \
	rpmdevtools \
	dnf-plugins-core

# Prepare RPM build structure
rpmdev-setuptree

echo "Downloading OpenWebStart"
echo "$OWS"

# Remove old deb file
[ -f /tmp/OpenWebStart.deb ] && rm -fv /tmp/OpenWebStart.deb

# Download
curl -#SLo /tmp/OpenWebStart.deb $OWS || { echo 'Download error..'; exit 1; }

# Create directory for archive
mkdir -p /tmp/OpenWebStart-${OWS_VER}

# Extract deb files into folder
ar --output /tmp/OpenWebStart-${OWS_VER} -x /tmp/OpenWebStart.deb

# Create tar archive for rpm
tar -czvf /root/rpmbuild/SOURCES/OpenWebStart-${OWS_VER}.tar.gz -C /tmp OpenWebStart-${OWS_VER}

# Copy RPM Spec into rpm SOURCE directory
cp OpenWebStart.spec /root/rpmbuild/SOURCES/

# Build rpm
rpmbuild -bb \
    --define "ows_version ${OWS_VER}" \
    --define "ows_release ${OWS_REL}" \
    /root/rpmbuild/SOURCES/OpenWebStart.spec

# Copy rpm into current(host) directory
cp /root/rpmbuild/RPMS/x86_64/OpenWebStart*.rpm .
