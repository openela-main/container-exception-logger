%global _hardened_build 1

Name: container-exception-logger
Version: 1.0.2
Release: 3%{?dist}
Summary: Logging from a container to a host

License: GPLv2+
URL: https://github.com/abrt/container-exception-logger
# source is created by:
# git clone https://github.com/abrt/container-exception-logger
# cd container-exception-logger; tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: libxslt
BuildRequires: git-core

## git format-patch -N 06aaa69 --start-number=1
Patch0001: 0001-Use-a-correct-command-name-in-helper.patch
Patch0002: 0002-Drop-the-setuid-wrapper.patch

%description
%{name} is a tool designed to run inside of
a container which is able to get its input outside of the container.

%prep
%autosetup -S git_am

%build
gcc %{build_cflags} %{build_ldflags} src/container-exception-logger.c -o src/container-exception-logger
a2x -d manpage -f manpage man/container-exception-logger.1.asciidoc

%install
mkdir -p %{buildroot}%{_bindir}
cp src/container-exception-logger %{buildroot}/%{_bindir}/container-exception-logger

mkdir -p %{buildroot}/%{_mandir}/man1
cp man/container-exception-logger.1 %{buildroot}/%{_mandir}/man1/container-exception-logger.1

%files
%{_bindir}/container-exception-logger
%{_mandir}/man1/container-exception-logger.1.*
%license COPYING

%changelog
* Thu Jul 4 2019 Martin Kutlak <mkutlak@redhat.com> 1.0.2-3
- Build with ldflags

* Thu Jun 13 2019 Martin Kutlak <mkutlak@redhat.com> 1.0.2-2
- Drop the setuid wrapper
- Use a correct command name in helper

* Mon Mar 26 2018 Matej Habrnal <mhabrnal@redhat.com> 1.0.2-1
- Use _hardened_build macro (mhabrnal@redhat.com)
- Add license (mhabrnal@redhat.com)

* Fri Mar 23 2018 Unknown name 1.0.1-1
- new package built with tito

* Thu Mar 08 2018 Matej Habrnal <mhabrnal@redhat.com> 1.0.0-1
- init
