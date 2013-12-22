%define upstream_name gitdb

Name: 		python-%{upstream_name}
Version: 	0.5.4
Release: 	1
Summary: 	Git Object Database
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/gitdb
Source0: 	http://pypi.python.org/packages/source/g/gitdb/gitdb-%{version}.tar.gz
BuildRequires:  python-distribute
BuildRequires:  python-async
BuildRequires:  python-smmap
Requires:       python-async
Requires:       python-smmap

%description
GitDB is a Python git object database.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --install-purelib=%{py_puresitedir}

rm -f %{buildroot}%{py_puresitedir}/gitdb/README
rm -f %{buildroot}%{py_puresitedir}/gitdb/AUTHORS

%files
%doc AUTHORS
%{py_platsitedir}/gitdb
%{py_platsitedir}/gitdb-%{version}-py%{py_ver}.egg-info
