%define pypi_name trio

Name:       python-%{pypi_name}
Version:    0.24.0
Release:    1
Summary:    A friendly Python library for async concurrency and I/O
License:    MIT or ASL 2.0
Group:      Development/Python
URL:        https://pypi.org/project/trio/
Source0:    https://files.pythonhosted.org/packages/source/t/trio/trio-%{version}.tar.gz
BuildArch:  noarch
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

%description
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python.  Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.  A web spider that wants to fetch lots of
pages in parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor monitoring
multiple subprocesses... that sort of thing.  Compared to other libraries, Trio
attempts to distinguish itself with an obsessive focus on usability and
correctness.  Concurrency is complicated; we try to make it easy to get things
right.}

%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%build
%py_build


%install
%py_install

%files 
