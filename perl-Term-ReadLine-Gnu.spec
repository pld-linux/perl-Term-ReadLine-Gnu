%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	ReadLine-Gnu
Summary:	Perl Term::ReadLine::Gnu module
Summary(pl):	Modu³ Perla Term::ReadLine::Gnu
Name:		perl-Term-ReadLine-Gnu
Version:	1.12
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	perl >= 5.6.1
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-perlprov >= 3.0.3-18
Provides:	perl(Term::ReadLine::Gnu::XS)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Term-Readline-Gnu

%description
Perl Term::ReadLine::Gnu module.

This is an implementation of the interface to the GNU Readline
Library. This module gives you input line editing facility, input
history management facility, word completion facility, etc. It uses
the real GNU Readline Library. And this module has the interface with
the almost all variables and functions which are documented in the GNU
Readline/History Library. So you can program your custom editing
function, your custom completion function, and so on with Perl. This
may be useful for prototyping before programming with C.

%description -l pl
Modu³ Perla Term::ReadLine::Gnu. Jest on implementacj± interfejsu do
biblioteki GNU Readline. Udostêpnia liniê wprowadzania tekstu z
mo¿liwo¶ci± edycji, zarz±dzania histori±, automatycznym dope³nianiem
itp. U¿ywa biblioteki GNU Readline, ma interfejs do prawie wszystkich
zmiennych i funkcji bibliotek Readline i History - mo¿na wiêc
oprogramowaæ w³asne funkcje edycji, dope³niania itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags} -DPERL_POLLUTE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_sitearch}/Term/ReadLine
%{perl_sitearch}/Term/ReadLine/Gnu*
%dir %{perl_sitearch}/auto/Term/ReadLine
%dir %{perl_sitearch}/auto/Term/ReadLine/Gnu
%attr(755,root,root) %{perl_sitearch}/auto/Term/ReadLine/Gnu/*.so
%{perl_sitearch}/auto/Term/ReadLine/Gnu/*.bs
%{perl_sitearch}/auto/Term/ReadLine/Gnu/XS
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
