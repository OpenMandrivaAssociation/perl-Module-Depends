%define upstream_name    Module-Depends
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Intrusive discovery of distribution dependencies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Chained)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(YAML)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Module::Depends extracts module dependencies from an unpacked distribution
tree.

Module::Depends only evaluates the META.yml shipped with a distribution.
This won't be effective until all distributions ship META.yml files, so we
suggest you take your life in your hands and look at
Module::Depends::Intrusive.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 655049
- rebuild for updated spec-helper

* Wed Feb 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 510522
- update to 0.15

* Tue Jun 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 391006
- import perl-Module-Depends


* Tue Jun 30 2009 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist

