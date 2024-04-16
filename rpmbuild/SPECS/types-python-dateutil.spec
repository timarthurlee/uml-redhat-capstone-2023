# Created by pyp2rpm-3.3.10
%global pypi_name types-python-dateutil
%global pypi_version 2.9.0.20240316

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Typing stubs for python-dateutil

License:        Apache-2.0 license
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Typing stubs for python-dateutilThis is a [PEP 561]( type stub package for the
[python-dateutil]( package. It can be used by type-checking tools like [mypy](
[pyright]( [pytype]( PyCharm, etc. to check code that uses python-dateutil.This
version of types-python-dateutil aims to provide accurate annotations for
python-dateutil2.9.*. The source for this package can be found at All fixes for

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 Typing stubs for python-dateutilThis is a [PEP 561]( type stub package for the
[python-dateutil]( package. It can be used by type-checking tools like [mypy](
[pyright]( [pytype]( PyCharm, etc. to check code that uses python-dateutil.This
version of types-python-dateutil aims to provide accurate annotations for
python-dateutil2.9.*. The source for this package can be found at All fixes for


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/dateutil-stubs
%{python3_sitelib}/types_python_dateutil-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 16 2024 brendanpham - 2.9.0.20240316-1
- Initial package.
