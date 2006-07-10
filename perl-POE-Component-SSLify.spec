#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-SSLify
Summary:	perl(POE::Component::SSLify)
Name:		perl-POE-Component-SSLify
Version:	0.04
Release:	0.1
# "same as perl" according to readme
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
#Patch0:		%{name}
# most of CPAN modules have generic URL (substitute pdir and pnam here)
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
This module makes Net::SSLeay's SSL sockets behave with POE :)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch0 -p1

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

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
# note it's mostly easier to copy unpackaged filelist here, and run adapter over the spec.
# use macros:
%{perl_vendorlib}/POE/Component/SSLify.pm
%dir %{perl_vendorlib}/POE/Component/SSLify
%{perl_vendorlib}/POE/Component/SSLify/*.pm
%{_mandir}/man3/*
