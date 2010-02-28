Summary:	Simple builder to facilitate programatic generation of XML markup
Summary(pl.UTF-8):	Proste narzędzie do budowania ułatwiające programowe generowanie znaczników XML
Name:		ruby-builder
Version:	2.1.2
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/21725/builder-%{version}.tgz
# Source0-md5:	31e6ecd35af1659272659610a51a8211
URL:		http://rubyforge.org/projects/builder
BuildRequires:	rpmbuild(macros) >= 1.277
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
Summary:	Documentation files for builder
Summary(pl.UTF-8):	Pliki dokumentacji do pakietu builder
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for builder.

%description rdoc -l pl.UTF-8
Pliki dokumentacji do pakietu builder.

%prep
%setup -q -n builder-%{version}

%build
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/blankslate.rb
%{ruby_rubylibdir}/builder
%{ruby_rubylibdir}/builder.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Builder
