%define upstream_name gitdb

Name: 		python-%{upstream_name}
Version: 	4.0.7
Release: 	1
Summary: 	Git Object Database
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/gitdb
Source0: 	http://pypi.python.org/packages/source/g/gitdb/gitdb-%{version}.tar.gz
BuildRequires:  python-distribute
BuildRequires:  python-smmap
Requires:       python-smmap

%description
GitDB is a Python git object database.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%py3_build

%install
%py3_install

rm -f %{buildroot}%{py_puresitedir}/gitdb/README
rm -f %{buildroot}%{py_puresitedir}/gitdb/AUTHORS

%files
%doc AUTHORS
%{python3_sitelib}/gitdb/
%{python3_sitelib}/gitdb-%{version}-py%{py_ver}.egg-info/
