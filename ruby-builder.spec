#
# Conditional build:
%bcond_without 	doc

%define	pkgname	builder
Summary:	Simple builder to facilitate programatic generation of XML markup
Summary(pl.UTF-8):	Proste narzędzie do budowania ułatwiające programowe generowanie znaczników XML
Name:		ruby-%{pkgname}
Version:	3.0.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	cf9d2693d684a749e35dda886c4dc23c
URL:		http://rubyforge.org/projects/builder
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Conflicts:	ruby-activesupport < 3.0.0
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarc only because of ruby packaging
%define		_enable_debug_packages	0

%description
Simple builder to facilitate programatic generation of XML markup.

%description -l pl.UTF-8
Proste narzędzie do budowania ułatwiające programowe generowanie
znaczników XML.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

%build
%if %{with doc}
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid
rm -r ri/{BlankSlate,Fixnum,Kernel,Module,Object,String}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
%if %{with doc}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/blankslate.rb
%{ruby_rubylibdir}/builder
%{ruby_rubylibdir}/builder.rb

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%endif

%if %{with doc}
%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Builder
%endif
