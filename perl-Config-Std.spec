#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-Std
Version  : 0.903
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRICKER/Config-Std-0.903.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRICKER/Config-Std-0.903.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libconfig-std-perl/libconfig-std-perl_0.903-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Config-Std-license = %{version}-%{release}
Requires: perl-Config-Std-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Std)

%description
Config::Std version 0.903
This module implements yet another damn configuration-file system.

%package dev
Summary: dev components for the perl-Config-Std package.
Group: Development
Provides: perl-Config-Std-devel = %{version}-%{release}
Requires: perl-Config-Std = %{version}-%{release}

%description dev
dev components for the perl-Config-Std package.


%package license
Summary: license components for the perl-Config-Std package.
Group: Default

%description license
license components for the perl-Config-Std package.


%package perl
Summary: perl components for the perl-Config-Std package.
Group: Default
Requires: perl-Config-Std = %{version}-%{release}

%description perl
perl components for the perl-Config-Std package.


%prep
%setup -q -n Config-Std-0.903
cd %{_builddir}
tar xf %{_sourcedir}/libconfig-std-perl_0.903-1.debian.tar.xz
cd %{_builddir}/Config-Std-0.903
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Config-Std-0.903/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-Std
cp %{_builddir}/Config-Std-0.903/LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-Std/a141ba1841c17a36680978fdefa7aba2ee0a0600
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Config-Std/c5f899f68b9dbf85a062f21f94e90de05ea49065
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::Std.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-Std/a141ba1841c17a36680978fdefa7aba2ee0a0600
/usr/share/package-licenses/perl-Config-Std/c5f899f68b9dbf85a062f21f94e90de05ea49065

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
