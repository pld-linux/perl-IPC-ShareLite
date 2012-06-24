%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	ShareLite
Summary:	IPC::ShareLite perl module
Summary(pl):	Modu� perla IPC::ShareLite
Name:		perl-IPC-ShareLite
Version:	0.08
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPC::ShareLite perl module.

%description -l pl
Modu� perla IPC::ShareLite.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes "" | perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
%{perl_sitearch}/auto/IPC/ShareLite/ShareLite.bs
%attr(755,root,root) %{perl_sitearch}/auto/IPC/ShareLite/ShareLite.so
%{_mandir}/man3/*
