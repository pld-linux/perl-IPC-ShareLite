%include	/usr/lib/rpm/macros.perl
Summary:	IPC-ShareLite perl module
Summary(pl):	Modu� perla IPC-ShareLite
Name:		perl-IPC-ShareLite
Version:	0.08
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/IPC-ShareLite-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC-ShareLite perl module.

%description -l pl
Modu� perla IPC-ShareLite.

%prep
%setup -q -n IPC-ShareLite-%{version}

%build
yes "" | perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/IPC/ShareLite.pm
%dir %{perl_sitearch}/auto/IPC/ShareLite
%{perl_sitearch}/auto/IPC/ShareLite/autosplit.ix
%{perl_sitearch}/auto/IPC/ShareLite/ShareLite.bs
%attr(755,root,root) %{perl_sitearch}/auto/IPC/ShareLite/ShareLite.so
%{_mandir}/man3/*
