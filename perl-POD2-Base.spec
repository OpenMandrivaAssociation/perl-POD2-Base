%define upstream_name    POD2-Base
%define upstream_version 0.043

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POD2/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is an abstraction of the code in POD2::IT and POD2::FR. These
modules belong to the Italian and the French translation projects of core
Perl pods.

Once a translation package had been installed, the translated documentation
can be accessed with:

    $ perldoc POD2::<lang>::<podname>

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


