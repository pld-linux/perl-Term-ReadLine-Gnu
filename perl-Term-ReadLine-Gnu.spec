#
# Conditional build:
%bcond_with	tests	# perform "make test" (require a working X connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ReadLine-Gnu
Summary:	Term::ReadLine::Gnu - Perl interface for the GNU Readline/History library
Summary(pl.UTF-8):	Term::ReadLine::Gnu - perlowy interfejs do biblioteki GNU Readline/History
Name:		perl-Term-ReadLine-Gnu
Version:	1.19
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e591287af62e000256893c84d01abebe
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Term-ReadLine-Gnu/
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Term::ReadLine::Gnu::XS)
Obsoletes:	perl-Term-Readline-Gnu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::ReadLine::Gnu Perl module is an implementation of the interface
to the GNU Readline Library. This module gives you input line editing
facility, input history management facility, word completion facility,
etc. It uses the real GNU Readline Library. And this module has the
interface with the almost all variables and functions which are
documented in the GNU Readline/History Library. So you can program
your custom editing function, your custom completion function, and so
on with Perl. This may be useful for prototyping before programming
with C.

%description -l pl.UTF-8
Moduł Perla Term::ReadLine::Gnu jest implementacją interfejsu do
biblioteki GNU Readline. Udostępnia linię wprowadzania tekstu z
możliwością edycji, zarządzania historią, automatycznym dopełnianiem
itp. Używa biblioteki GNU Readline, ma interfejs do prawie wszystkich
zmiennych i funkcji bibliotek Readline i History - można więc
oprogramować własne funkcje edycji, dopełniania itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -DPERL_POLLUTE"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} \
	CC="%{__cc}" \
	install DESTDIR=$RPM_BUILD_ROOT
rm -f eg/*.orig
install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorarch}/Term/ReadLine
%{perl_vendorarch}/Term/ReadLine/Gnu*
%dir %{perl_vendorarch}/auto/Term/ReadLine
%dir %{perl_vendorarch}/auto/Term/ReadLine/Gnu
%attr(755,root,root) %{perl_vendorarch}/auto/Term/ReadLine/Gnu/*.so
%{perl_vendorarch}/auto/Term/ReadLine/Gnu/*.bs
# empty autosplit.ix, but requred
%dir %{perl_vendorarch}/auto/Term/ReadLine/Gnu/XS
%{perl_vendorarch}/auto/Term/ReadLine/Gnu/XS/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
