%include	/usr/lib/rpm/macros.perl
Summary:	Perl Term::ReadLine::Gnu module
Summary(pl):	Modu³ Perla Term::ReadLine::Gnu
Name:		perl-Term-ReadLine-Gnu
Version:	1.08
Release:	2
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/Term-ReadLine-Gnu-%{version}.tar.gz
Patch0:		perl-Term-ReadLine-Gnu-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
%requires_eq	perl
Requires:	%{perl_sitearch}
Provides:	perl(Term::ReadLine::Gnu::XS)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Term::ReadLine::Gnu module.

%description -l pl
Modu³ Perla Term::ReadLine::Gnu.

%prep
%setup -q -n Term-ReadLine-Gnu-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS -DPERL_POLLUTE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install eg/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

strip --strip-unneeded \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Term/ReadLine/Gnu/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Term/ReadLine/Gnu
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/Term/ReadLine/Gnu*

%dir %{perl_sitearch}/auto/Term/ReadLine/Gnu
%attr(755,root,root) %{perl_sitearch}/auto/Term/ReadLine/Gnu/*.so
%{perl_sitearch}/auto/Term/ReadLine/Gnu/*.bs
%{perl_sitearch}/auto/Term/ReadLine/Gnu/XS
%{perl_sitearch}/auto/Term/ReadLine/Gnu/.packlist

%{_mandir}/man3/*
%{_prefix}/src/examples/%{name}
