%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

Name:           OpenWebStart
Version:        %{ows_version}
Release:        %{ows_release}%{?dist}
Summary:        OpenWebStart offers a user-friendly installer to use Web Start / JNLP functionality
Packager:	Fatih Usta <fatihusta86@gmail.com>

License:        GPLv2
URL:            https://github.com/karakun/OpenWebStart 
Source0:        %{name}-%{version}.tar.gz
NoSource: 0
Requires:      shared-mime-info, xdg-utils


%description
Java Web Start (JWS) was deprecated in Java 9, and starting with Java 11,
Oracle removed JWS from their JDK distributions. This means that clients
that have the latest version of Java installed can no longer use JWS-based
applications. And since public support of Java 8 has ended in Q2/2019,
companies no longer get any updates and security fixes for Java Web Start.

OpenWebStart offers a user-friendly installer to use Web Start / JNLP functionality
with future Java versions without depending on a specific Java vendor or distribution.
The first goal of the project is to target Java 8 LTS versions while support for
Java 11 LTS will come in near future.

While we (Karakun) develop user-friendly installers to use a Java vendor–independent
approach for Web Start, we also help to integrate Web Start functionally
in the Java 8 LTS releases of AdoptOpenJDK. Therefore all Web Start functionality
is developed in the IcedTea-Web repository of the AdoptOpenJDK organization together
with Red Hat and other members of the AdoptOpenJDK community. Therefore this 
repository only contains sources that are needed to create enterprise-ready 
and user-friendly native installers for OpenWebStart.

%prep
%autosetup -p1


%build
echo 'Using pre builded debian package'

%install
mkdir -p  %{buildroot}/opt/%{name}/control
tar -xf $RPM_BUILD_DIR/%{name}-%{version}/data.tar.gz -C %{buildroot}/
tar -xf $RPM_BUILD_DIR/%{name}-%{version}/control.tar.gz -C %{buildroot}/opt/%{name}/control

%post
if [ $1 = 1 ]; then # First install
    echo 'Configuring...'
    /opt/%{name}/control/postinst 'configure' || :
fi

%preun
if [ $1 = 0 ]; then # uninstall
    echo 'Uninstalling...'
    /opt/%{name}/control/prerm 'remove' || :
fi

%files
/opt/%{name}/

%changelog
* Fri Jul 22 2022 Fatih USTA <fatihusta86@gmail.com>
- Initial build

