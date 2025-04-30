%define debug_package %{nil}
%define pypi_name gitdb

Name: 		python-%{pypi_name}
Version: 	4.0.12
Release: 	1
Summary: 	Git Object Database
License:	BSD
Group: 		Development/Python
Url: 		https://pypi.python.org/pypi/gitdb
Source0: 	https://files.pythonhosted.org/packages/source/g/gitdb/gitdb-%{version}.tar.gz
BuildRequires:  python-distribute
BuildRequires:  python-smmap
Requires:       python-smmap

%description
GitDB is a Python git object database.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc AUTHORS
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{py_ver}.egg-info
