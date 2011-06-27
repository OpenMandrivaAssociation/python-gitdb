%define upstream_name gitdb
%define name    python-%{upstream_name}
%define version 0.5.2
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Git Object Database
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/gitdb
Source0: 	http://pypi.python.org/packages/source/g/gitdb/gitdb-%{version}.tar.gz
Patch0:     gitdb-0.5.2-fix_symbol_visibility.patch 
BuildRequires:  python-distribute
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
GitDB is a Python git object database.

%prep
%setup -q -n %upstream_name-%version
%patch -p0 
%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

rm -f %{buildroot}%{python_sitelib}/gitdb/README
rm -f %{buildroot}%{python_sitelib}/gitdb/AUTHORS

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{python_sitearch}/gitdb
%{python_sitearch}/gitdb-%{version}-py%{pyver}.egg-info
