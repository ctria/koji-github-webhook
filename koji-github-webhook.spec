Name: koji-github-webhook
Version: 0.2
Release: 1%{?dist}
License: LGPLv2
Summary: A github webhook for koji
Group: Applications/System
URL: http://github.com/ctria/koji-github-webhook
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: httpd
Requires: mod_wsgi
Requires: koji

%description
A github webhook for koji

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT %{?install_opt} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/koji-github-webhook
%dir %{_sysconfdir}/koji-github-webhook
%config(noreplace) %{_sysconfdir}/koji-github-webhook/koji-github-webhook.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/koji-github-webhook.conf

%changelog
* Sun Jul 16 2017 Christos Triantafyllidis <christos.triantafyllidis at gmail.com> - 0.2
- Added a configuration option for scratch builds

* Wed Aug 12 2015 Christos Triantafyllidis <christos.triantafyllidis at gmail.com> - 0.1
- Initial release
