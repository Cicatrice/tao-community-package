%define mathjax_version %(echo $MJ_VERSION)

Name:           tao-community-mathjax
Version:        %{mathjax_version}
Release:        0
Summary:        MathJax depedencies for TAO Community edition
License:        Apache v2
URL:            https://www.mathjax.org/
Source0:        MathJax-%{version}.tar.gz

BuildArch:      noarch
#BuildRequires:
Requires:       tao-community
#Requires(build): composer

%description
TAO is the first commercial-grade Open Source assessment development software on the market. It is QTI and LTI standards-based, and operates under audit-proof transparency. Developers can access the source code for their own test-creating or administering purposes, opening the user to a wide range of potential customizations. Complete ownership of test design has never been this easy; without the restrictions and high costs of proprietary testing, all assessments can easily be displayed with the educational institution's signature details. Furthermore, TAO is fully compatible with just about all of your favorite commercial add-ons.

%global debug_package %{nil}

%prep

%setup -c

%build

%install
mkdir -p                                                         \
 %{buildroot}/%{_datadir}/tao-community/taoQtiItem/views/js/mathjax

mv *  \
 %{buildroot}/%{_datadir}/tao-community/taoQtiItem/views/js/mathjax

%clean
rm -rf %{buildroot}

%files
 %{_datadir}/tao-community/taoQtiItem/views/js/mathjax
#%license %{_datadir}/%{name}/LICENSE

%pre

%post
chown -R taosrv %{_datadir}/tao-community

%postun
case "$1" in
   0) # This is a yum remove.
   ;;
   1) # This is a yum upgrade.
      # do nothing
   ;;
 esac

%changelog
* Thu Apr 27 2017 Geoffrey Gouez <geoffrey@taotesting.com>
-
