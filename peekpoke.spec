# Build this using apx-rpmbuild.
%define name peekpoke

Name:           %{name}
Version:        %{version_rpm_spec_version}
Release:        %{version_rpm_spec_release}%{?dist}
Summary:        A simple peek/poke command from Xilinx.

License:        Reserved
URL:            https://github.com/uwcms/APx-%{name}
Source0:        %{name}-%{version_rpm_spec_version}.tar.gz

%global debug_package %{nil}

%description
This package provides a simple peek/poke command from Xilinx.


%prep
%setup -q


%build
##configure
make %{?_smp_mflags} LIB_VERSION=%{version_sofile}


%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 peek %{buildroot}/%{_bindir}/peek
install -D -m 0755 poke %{buildroot}/%{_bindir}/poke


%files
%{_bindir}/peek
%{_bindir}/poke

%changelog
* Tue Jan 14 2020 Jesra Tikalsky <jtikalsky@hep.wisc.edu>
- Initial spec file
