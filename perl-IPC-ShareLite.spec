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
Version:	0.09
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3942a55cfc5e6d3b612a46cc1a9515b9
Patch0:		%{name}-types.patch
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
%patch0 -p1

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
%doc Changes README TODO
%{perl_vendorarch}/IPC/ShareLite.pm
%dir %{perl_vendorarch}/auto/IPC/ShareLite
%{perl_vendorarch}/auto/IPC/ShareLite/autosplit.ix
%{perl_vendorarch}/auto/IPC/ShareLite/ShareLite.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IPC/ShareLite/ShareLite.so
%{_mandir}/man3/*
