%global pypi_name numba
%global pypi_version 0.59.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        compiling Python code using LLVM

License:        BSD
URL:            https://numba.pydata.org
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  (python3dist(llvmlite) >= 0.42~~dev0 with python3dist(llvmlite) < 0.43~~)
BuildRequires:  (python3dist(numpy) >= 1.11 with python3dist(numpy) < 1.27~~)
BuildRequires:  (python3dist(numpy) >= 1.22 with python3dist(numpy) < 1.27~~)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
 A Just-In-Time Compiler for Numerical Functions in Python

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(llvmlite) >= 0.42~~dev0 with python3dist(llvmlite) < 0.43~~)
Requires:       (python3dist(numpy) >= 1.22 with python3dist(numpy) < 1.27~~)

%description -n python3-%{pypi_name}
 A Just-In-Time Compiler for Numerical Functions in Python

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
#PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE LICENSES.third-party
%doc README.rst docs/upcoming_changes/README.rst
%{_bindir}/numba
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%license LICENSE LICENSES.third-party

%changelog
* Tue Feb 20 2024 Tim Lee <timarthurlee@gmail.com> - 0.59.0-1
- Initial package.
