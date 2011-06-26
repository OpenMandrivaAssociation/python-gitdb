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
BuildRequires:  python-distribute
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
GitDB is a pure-Python git object database.

%prep
%setup -q -n %upstream_name-%version

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
%{python_sitelib}/gitdb
%{python_sitelib}/gitdb-%{version}-py%{pyver}.egg-info
