#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	ShareLite
Summary:	IPC::ShareLite Perl module
Summary(cs):	Modul IPC::ShareLite pro Perl
Summary(da):	Perlmodul IPC::ShareLite
Summary(de):	IPC::ShareLite Perl Modul
Summary(es):	Módulo de Perl IPC::ShareLite
Summary(fr):	Module Perl IPC::ShareLite
Summary(it):	Modulo di Perl IPC::ShareLite
Summary(ja):	IPC::ShareLite Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	IPC::ShareLite ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul IPC::ShareLite
Summary(pl):	Modu³ Perla IPC::ShareLite
Summary(pt):	Módulo de Perl IPC::ShareLite
Summary(pt_BR):	Módulo Perl IPC::ShareLite
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl IPC::ShareLite
Summary(sv):	IPC::ShareLite Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl IPC::ShareLite
Summary(zh_CN):	IPC::ShareLite Perl Ä£¿é
Name:		perl-IPC-ShareLite
Version:	0.09
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::ShareLite provides a simple interface to shared memory, allowing
data to be efficiently communicated between processes. Your operating
system must support SysV IPC (shared memory and semaphores) in order
to use this module.

%description -l pl
IPC::ShareLite udostêpnia prosty interfejs do pamiêci wspólnej,
umo¿liwaiaj±c wydajn± wymianê danych pomiêdzy procesami. Aby
korzystanie z tego modu³u by³o mo¿liwe, System operacyjny musi
wspieraæ SysV IPC (pamiêæ wspólna i semafory).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL </dev/null
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_sitearch}/IPC/ShareLite.pm
%dir %{perl_sitearch}/auto/IPC/ShareLite
%{perl_sitearch}/auto/IPC/ShareLite/autosplit.ix
%{perl_sitearch}/auto/IPC/ShareLite/ShareLite.bs
%attr(755,root,root) %{perl_sitearch}/auto/IPC/ShareLite/ShareLite.so
%{_mandir}/man3/*
