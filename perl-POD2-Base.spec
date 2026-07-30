%define upstream_name    POD2-Base
%define upstream_version 0.043
Name:		perl-%{upstream_name}
Version:	0.043
Release:	1

Summary:	This module is an abstraction of the code in POD2::IT and POD2::FR
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/POD2-Base-0.043.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildArch:	noarch

%description
This module is an abstraction of the code in POD2::IT and POD2::FR. These
modules belong to the Italian and the French translation projects of core
Perl pods.

Once a translation package had been installed, the translated documentation
can be accessed with:

    $ perldoc POD2::<lang>::<podname>

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

