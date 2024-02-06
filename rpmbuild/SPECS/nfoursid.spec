%global pypi_name nfoursid
%global pypi_version 1.0.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Implementation of N4SID, Kalman filtering and state-space models

License:        MIT
URL:            https://github.com/spmvg/nfoursid
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib) >= 3.3
BuildRequires:  python3dist(numpy) >= 1.19
BuildRequires:  python3dist(pandas) >= 1.1
BuildRequires:  python3dist(setuptools)

%description
 NFourSIDImplementation of the N4SID algorithm for subspace identification [1],
together with Kalman filtering and state-space State-space models are versatile
models for representing multi-dimensional timeseries. As an example, the
ARMAX(_p_, _q_, _r_)-models - AutoRegressive MovingAverage with eXogenous input
- are included in the representation of state-space models. By extension,
ARMA-,...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(matplotlib) >= 3.3
Requires:       python3dist(numpy) >= 1.19
Requires:       python3dist(pandas) >= 1.1
%description -n python3-%{pypi_name}
 NFourSIDImplementation of the N4SID algorithm for subspace identification [1],
together with Kalman filtering and state-space State-space models are versatile
models for representing multi-dimensional timeseries. As an example, the
ARMAX(_p_, _q_, _r_)-models - AutoRegressive MovingAverage with eXogenous input
- are included in the representation of state-space models. By extension,
ARMA-,...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 06 2024 Tim Lee - 1.0.1-1
- Initial package.
