#
# Conditional build:
%bcond_with	tests	# perform "make test" (require a working X connection)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ReadLine-Gnu
Summary:	Term::ReadLine::Gnu Perl module
Summary(cs.UTF-8):	Modul Term::ReadLine::Gnu pro Perl
Summary(da.UTF-8):	Perlmodul Term::ReadLine::Gnu
Summary(de.UTF-8):	Term::ReadLine::Gnu Perl Modul
Summary(es.UTF-8):	Módulo de Perl Term::ReadLine::Gnu
Summary(fr.UTF-8):	Module Perl Term::ReadLine::Gnu
Summary(it.UTF-8):	Modulo di Perl Term::ReadLine::Gnu
Summary(ja.UTF-8):	Term::ReadLine::Gnu Perl モジュール
Summary(ko.UTF-8):	Term::ReadLine::Gnu 펄 모줄
Summary(nb.UTF-8):	Perlmodul Term::ReadLine::Gnu
Summary(pl.UTF-8):	Moduł Perla Term::ReadLine::Gnu
Summary(pt.UTF-8):	Módulo de Perl Term::ReadLine::Gnu
Summary(pt_BR.UTF-8):	Módulo Perl Term::ReadLine::Gnu
Summary(ru.UTF-8):	Модуль для Perl Term::ReadLine::Gnu
Summary(sv.UTF-8):	Term::ReadLine::Gnu Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Term::ReadLine::Gnu
Summary(zh_CN.UTF-8):	Term::ReadLine::Gnu Perl 模块
Name:		perl-Term-ReadLine-Gnu
Version:	1.17a
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	acdd3ded64423390824f31149ebfdf5c
Patch0:		%{name}-paths.patch
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Term::ReadLine::Gnu::XS)
Obsoletes:	perl-Term-Readline-Gnu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Moduł Perla Term::ReadLine::Gnu. Jest on implementacją interfejsu do
biblioteki GNU Readline. Udostępnia linię wprowadzania tekstu z
możliwością edycji, zarządzania historią, automatycznym dopełnianiem
itp. Używa biblioteki GNU Readline, ma interfejs do prawie wszystkich
zmiennych i funkcji bibliotek Readline i History - można więc
oprogramować własne funkcje edycji, dopełniania itp.

%prep
%setup -q -n %{pdir}-%{pnam}-1.17
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
