%global pypi_name holidays
%global pypi_version 0.41

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Generate and work with holidays in Python

License:        MIT License

URL:            None
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(python-dateutil)

%description
 python-holidays A fast, efficient Python library for generating country- and
subdivision- (e.g. state or province) specific sets of government-designated
holidays on the fly. It aims to make determining whether a specific date is a
holiday as fast and flexible as possible.:PyPI: :alt: PyPI version

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(python-dateutil)
%description -n python3-%{pypi_name}
 python-holidays A fast, efficient Python library for generating country- and
subdivision- (e.g. state or province) specific sets of government-designated
holidays on the fly. It aims to make determining whether a specific date is a
holiday as fast and flexible as possible.:PyPI: :alt: PyPI version

%package -n python-%{pypi_name}-doc
Summary:        holidays documentation
%description -n python-%{pypi_name}-doc
Documentation for holidays

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Jan 23 2024 Tim Lee <timarthurlee@gmail.com> - 0.41-1
- Initial package.
