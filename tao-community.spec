%define tao_version %(echo $TAO_VERSION)

Name:           tao-community
Version:        %{tao_version}
Release:        0
Summary:        Open-Source Testing and Assessment authoring and delivery software
License:        GNU GPL v2
URL:            https://hub.taocloud.org/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
#BuildRequires:
Requires:       php-fpm php-mysqlnd php-pgsql
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel
#Requires(build): composer

%description
TAO is the first commercial-grade Open Source assessment development software on the market. It is QTI and LTI standards-based, and operates under audit-proof transparency. Developers can access the source code for their own test-creating or administering purposes, opening the user to a wide range of potential customizations. Complete ownership of test design has never been this easy; without the restrictions and high costs of proprietary testing, all assessments can easily be displayed with the educational institution's signature details. Furthermore, TAO is fully compatible with just about all of your favorite commercial add-ons.

%global debug_package %{nil}

%prep

%setup -c

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install .htaccess * %{buildroot}%{_datadir}/%{name}
#rm -rf %{buildroot}/%{_datadir}/%{name}/taoqtiitem/views/js/portablesharedlibraries %{buildroot}/%{_datadir}/%{name}/tao/views/locales
mkdir -p                                                     \
 %{buildroot}/%{_sysconfdir}/%{name}                             \
 %{buildroot}/%{_sharedstatedir}/%{name}/portablesharedlibraries \
 %{buildroot}/%{_sharedstatedir}/%{name}/files                   \
 %{buildroot}/%{_sharedstatedir}/%{name}/locales

%clean
rm -rf %{buildroot}

%files
%license LICENSE
%{_datadir}/%{name}/
%{_sharedstatedir}/%{name}/files/
%config(noreplace) %{_sysconfdir}/%{name}/

%pre
/usr/bin/getent group taosrv > /dev/null  || /usr/sbin/groupadd -r taosrv
/usr/bin/getent passwd taosrv > /dev/null || /usr/sbin/useradd -r -d %{_datadir}/%{name} -s /sbin/nologin -g taosrv taosrv

%post
ln -fs %{_sharedstatedir}/%{name}/files %{_datadir}/%{name}/data
ln -fs %{_sysconfdir}/%{name} %{_datadir}/%{name}/config
ln -fs %{_sharedstatedir}/%{name}/portableSharedLibraries %{_datadir}/%{name}/taoQtiItem/views/js/portableSharedLibraries
ln -fs %{_sharedstatedir}/%{name}/locales %{_datadir}/%{name}/tao/views/locales

%postun
case "$1" in
   0) # This is a yum remove.
      /usr/sbin/userdel taosrv
   ;;
   1) # This is a yum upgrade.
      # do nothing
   ;;
 esac

%changelog
* Thu Apr 27 2017 Geoffrey Gouez <geoffrey@taotesting.com>
-
