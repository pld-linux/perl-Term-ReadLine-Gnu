%include	/usr/lib/rpm/macros.perl
Summary:	Perl Term::ReadLine::Gnu module
Summary(pl):	Modu³ Perla Term::ReadLine::Gnu
Name:		perl-Term-ReadLine-Gnu
Version:	1.07
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term-ReadLine-Gnu-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Perl Term::ReadLine::Gnu module.

%description -l pl
Modu³ Perla Term::ReadLine::Gnu.

%prep
%setup -q -n Term-ReadLine-Gnu-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS -DPERL_POLLUTE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Term/ReadLine/Gnu
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/Term/ReadLine/Gnu*

%dir %{perl_sitearch}/auto/Term/ReadLine/Gnu

%attr(755,root,root) %{perl_sitearch}/auto/Term/ReadLine/Gnu/*.so

%{perl_sitearch}/auto/Term/ReadLine/Gnu/*.bs
%{perl_sitearch}/auto/Term/ReadLine/Gnu/XS
%{perl_sitearch}/auto/Term/ReadLine/Gnu/.packlist

%{_mandir}/man3/*
