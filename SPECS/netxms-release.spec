Name:           netxms-release
Version:        1
Release:        1%{dist}
Summary:        NetXMS Packages for Enterprise Linux repository configuration
License:        GPLv2

URL:            https://github.com/netxms/packages-rpm-release
Source0:        https://packages.netxms.org/epel/RPM-GPG-KEY-NETXMS
Source1:        GPL

Source100:      netxms.repo

BuildArch:      noarch

%description
This package contains the NetXMS Packages for Enterprise Linux repository
GPG key as well as configuration for yum.


%prep
%setup -q -c -T
install -pm 644 %{SOURCE1} .

%install
install -Dpm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-NETXMS
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE100} %{buildroot}%{_sysconfdir}/yum.repos.d

%post


%files
%license GPL
%config(noreplace) %{_sysconfdir}/yum.repos.d/netxms.repo
%{_sysconfdir}/pki/rpm-gpg/*


%changelog
* Fri Sep 30 2022 Alex Kirhenshtein <alk@netxms.org> - 1-1
- Initial version
