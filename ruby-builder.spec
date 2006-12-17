Summary:	Simple builder to facilitate programatic generation of XML markup
Summary(pl):	Proste narzêdzie do budowania u³atwiaj±ce programowe generowanie znaczników XML
Name:		ruby-builder
Version:	2.0.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/8400/builder-%{version}.gem
# Source0-md5:	bd2bdac16b851ee482372e9d8c5a1c94
URL:		http://code.whytheluckystiff.net/builder/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple builder to facilitate programatic generation of XML markup.

%description -l pl
Proste narzêdzie do budowania u³atwiaj±ce programowe generowanie
znaczników XML.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/builder*
#%{ruby_ridir}/*
