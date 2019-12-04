#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	ShareLite
Summary:	IPC::ShareLite Perl module - light-weight interface to shared memory
Summary(pl.UTF-8):	Moduł Perla IPC::ShareLite - lekki interfejs do pamięci dzielonej
Name:		perl-IPC-ShareLite
Version:	0.17
Release:	14
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IPC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	54c7aa08dc065b6c946c48491d33450d
URL:		http://search.cpan.org/dist/IPC-ShareLite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::ShareLite provides a simple interface to shared memory, allowing
data to be efficiently communicated between processes. Your operating
system must support SysV IPC (shared memory and semaphores) in order
to use this module.

%description -l pl.UTF-8
IPC::ShareLite udostępnia prosty interfejs do pamięci wspólnej,
umożliwiając wydajną wymianę danych pomiędzy procesami. Aby
korzystanie z tego modułu było możliwe, System operacyjny musi
wspierać SysV IPC (pamięć wspólna i semafory).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/IPC/ShareLite.pm
%dir %{perl_vendorarch}/auto/IPC/ShareLite
%{perl_vendorarch}/auto/IPC/ShareLite/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/IPC/ShareLite/ShareLite.so
%{_mandir}/man3/*
