%define tao_version %(echo $TAO_VERSION)

Name:           tao-community
Version:        %{tao_version}
Release:        0
Summary:        Open Source assessment development software
License:        GNU GPL v2
URL:            https://hub.taocloud.org/
Source0:        %{name}-%{version}.tar.gz
#Source0:        source
#Source0:	http://gogs.cicatrice.eu/cicatrice/tao-community-package/archive/v%{version}.tar.gz

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
#%setup -q -n tao-community-package

%build
#echo Start build
##mkdir -p %{buildroot}
##cp -a source/app %{buildroot}/
#cp -R ../LICENSE  %{buildroot}/
#pushd source/app
##pushd %{buildroot}/app
#composer install
#rm composer.json composer.lock
#popd

%install
mkdir -p %{buildroot}%{_datadir}/tao
install -d . %{buildroot}/%{_datadir}/tao
rm -rf %{buildroot}/%{_datadir}/tao/taoqtiitem/views/js/portablesharedlibraries %{buildroot}/%{_datadir}/tao/tao/views/locales
mkdir -p                                                     \
 %{buildroot}/%{_sysconfdir}/tao                             \
 %{buildroot}/%{_sharedstatedir}/tao/db                      \
 %{buildroot}/%{_sharedstatedir}/tao/portablesharedlibraries \
 %{buildroot}/%{_sharedstatedir}/tao/files                   \
 %{buildroot}/%{_sharedstatedir}/tao/locales

## mkdir -p %{buildroot}/%{_datadir}/
## rm -rf %{buildroot}/%{_datadir}/tao
## mv %{buildroot}/app %{buildroot}/%{_datadir}/tao
## rm -rf %{buildroot}/%{_datadir}/tao/taoqtiitem/views/js/portablesharedlibraries %{buildroot}/%{_datadir}/tao/tao/views/locales
## mkdir -p                                                      \
##   %{buildroot}/%{_sysconfdir}/tao                             \
##   %{buildroot}/%{_sharedstatedir}/tao/db                      \
##   %{buildroot}/%{_sharedstatedir}/tao/portablesharedlibraries \
##   %{buildroot}/%{_sharedstatedir}/tao/files                   \
##   %{buildroot}/%{_sharedstatedir}/tao/locales

#rm -rf %{buildroot}

%clean
rm -rf %{buildroot}
echo welcome package %{_rpmfilename}
env | grep rpm

%files
#%license LICENSE
%{_datadir}/tao/
%{_sharedstatedir}/tao/db/
%{_sharedstatedir}/tao/files/
%config(noreplace) %{_sysconfdir}/tao/

%pre
/usr/bin/getent group taosrv > /dev/null  || /usr/sbin/groupadd -r taosrv
/usr/bin/getent passwd taosrv > /dev/null || /usr/sbin/useradd -r -d %{_datadir}/tao -s /sbin/nologin -g taosrv taosrv

%post
ln -fs %{_sharedstatedir}/tao/files %{_datadir}/tao/data
ln -fs %{_sysconfdir}/tao %{_datadir}/tao/config
ln -fs %{_sharedstatedir}/tao/portableSharedLibraries %{_datadir}/tao/taoQtiItem/views/js/portableSharedLibraries
ln -fs %{_sharedstatedir}/tao/locales %{_datadir}/tao/tao/views/locales

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
