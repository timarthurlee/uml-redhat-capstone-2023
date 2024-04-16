# Created by pyp2rpm-3.3.8
%global pypi_name Arrow
%global pypi_version 1.3.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Better dates & times for Python

License:  Apache-2.0

URL:            None
Source0:        https://files.pythonhosted.org/packages/source/A/%{pypi_name}/arrow-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(dateparser) >= 1 with python3dist(dateparser) < 2)
BuildRequires:  python3dist(doc8)
BuildRequires:  python3dist(pre-commit)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(python-dateutil) >= 2.7
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  (python3dist(simplejson) >= 3 with python3dist(simplejson) < 4)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autobuild)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinx-rtd-theme) 
BuildRequires:  python3dist(types-python-dateutil) 

%description
Arrow: Better dates & times for Python .. start-inclusion-marker-do-not-remove
.. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(dateparser) >= 1 with python3dist(dateparser) < 2)
Requires:       python3dist(pre-commit)
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-mock)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(pytz)
Requires:       python3dist(simplejson)
Requires:       python3dist(types-python-dateutil) 
%description -n python3-%{pypi_name}
Arrow: Better dates & times for Python .. start-inclusion-marker-do-not-remove
.. image::


%prep
%autosetup -n arrow-%{pypi_version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/arrow
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 20 2024 brendanpham - 1.3.0-1
- Initial package.
