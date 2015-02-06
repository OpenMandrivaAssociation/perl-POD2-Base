%define upstream_name    POD2-Base
%define upstream_version 0.043

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	This module is an abstraction of the code in POD2::IT and POD2::FR
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POD2/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.43.0-2mdv2011.0
+ Revision: 657808
- rebuild for updated spec-helper

* Sat Sep 18 2010 Shlomi Fish <shlomif@mandriva.org> 0.43.0-1mdv2011.0
+ Revision: 579593
- import perl-POD2-Base

