#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-SSLify
Summary:	POE::Component::SSLify - make using SSL in the world of POE easy
Summary(pl):	POE::Component::SSLify - �atwe u�ywanie SSL-a w �wiecie POE
Name:		perl-POE-Component-SSLify
Version:	0.04
Release:	1
# "same as perl" according to readme
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c3a9c5d538453105e20b2a3a0fce183
URL:		http://search.cpan.org/dist/POE-Component-SSLify/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes Net::SSLeay's SSL sockets behave with POE.

%description -l pl
Ten modu� pozwala na wsp�prac� gniazd SSL z Net::SSLeay z POE.

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
%doc README
%{perl_vendorlib}/POE/Component/SSLify.pm
%dir %{perl_vendorlib}/POE/Component/SSLify
%{perl_vendorlib}/POE/Component/SSLify/*.pm
%{_mandir}/man3/*
