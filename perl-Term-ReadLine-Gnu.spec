%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	ReadLine-Gnu
Summary:	Perl Term::ReadLine::Gnu module
Summary(pl):	Modu³ Perla Term::ReadLine::Gnu
Name:		perl-Term-ReadLine-Gnu
Version:	1.12
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6.1
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
Provides:	perl(Term::ReadLine::Gnu::XS)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Term-Readline-Gnu

%description
Perl Term::ReadLine::Gnu module.

%description -l pl
Modu³ Perla Term::ReadLine::Gnu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags} -DPERL_POLLUTE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Term/ReadLine/Gnu*
%dir %{perl_sitearch}/auto/Term/ReadLine/Gnu
%attr(755,root,root) %{perl_sitearch}/auto/Term/ReadLine/Gnu/*.so
%{perl_sitearch}/auto/Term/ReadLine/Gnu/*.bs
%{perl_sitearch}/auto/Term/ReadLine/Gnu/XS
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
