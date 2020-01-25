#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Password-Pronounceable
Summary:	Text::Password::Pronounceable - Generate pronounceable passwords
#Summary(pl.UTF-8):	
Name:		perl-Text-Password-Pronounceable
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a6a3c9197dfb5912f763c0c4f285b48
URL:		http://search.cpan.org/dist/Text-Password-Pronounceable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module generates pronuceable passwords, based the the English
digraphs by D Edwards.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Text/Password/*.pm
%{_mandir}/man3/*
