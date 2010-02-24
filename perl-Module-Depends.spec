%define upstream_name    Module-Depends
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Intrusive discovery of distribution dependencies
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Chained)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


