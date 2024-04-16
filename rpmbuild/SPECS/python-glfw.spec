%global pypi_name glfw
%global pypi_version 2.7.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A ctypes-based wrapper for GLFW3

License:        MIT
URL:            https://github.com/FlorianRhiem/pyGLFW
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This module provides Python bindings for GLFW < (on GitHub: glfw/glfw < It is a
ctypes wrapper which keeps very close to the original GLFW API, except for:-
function names use the pythonic words_with_underscores notation instead of
camelCase - GLFW_ and glfw prefixes have been removed, as their function is
replaced by the module namespace (you can use from glfw.GLFW import * if you
prefer the...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(glfw-preview)
%description -n python3-%{pypi_name}
This module provides Python bindings for GLFW < (on GitHub: glfw/glfw < It is a
ctypes wrapper which keeps very close to the original GLFW API, except for:-
function names use the pythonic words_with_underscores notation instead of
camelCase - GLFW_ and glfw prefixes have been removed, as their function is
replaced by the module namespace (you can use from glfw.GLFW import * if you
prefer the...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 16 2024 Tim Lee <timarthurlee@gmail.com> - 2.7.0-1
- Initial package.
