%define		module	pyclip
Summary:	Cross-platform clipboard utilities supporting both binary and text data
Name:		python3-%{module}
Version:	0.7.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pyclip/%{module}-%{version}.tar.gz
# Source0-md5:	6f03fc99b9885686b8868798e027fd8e
Patch0:		build.patch
URL:		https://pypi.org/project/pyclip/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-platform clipboard utilities supporting both binary and text
data.

%prep
%setup -q -n %{module}-%{version}
%patch -P 0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/pyclip
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
