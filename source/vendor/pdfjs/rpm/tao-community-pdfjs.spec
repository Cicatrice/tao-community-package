%define pdfjs_version %(echo $PJ_VERSION)

Name:           tao-community-pdfjs
Version:        %{pdfjs_version}
Release:        0
Summary:        PDF.js add-ons for TAO Community edition
License:        Apache v2
URL:            https://mozilla.github.io/pdf.js/
Source0:        pdfjs-%{version}.tar.gz

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
 %{buildroot}/%{_datadir}/tao-community/tao/views/js/lib/pdfjs

mv *  \
 %{buildroot}/%{_datadir}/tao-community/tao/views/js/lib/pdfjs

%clean
rm -rf %{buildroot}

%files
 %{_datadir}/tao-community/tao/views/js/lib/pdfjs
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
