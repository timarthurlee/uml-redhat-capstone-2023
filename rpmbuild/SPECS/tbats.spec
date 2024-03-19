%global pypi_name tbats
%global pypi_version 1.1.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        BATS and TBATS for time series forecasting

License:        MIT License
URL:            https://github.com/intive-DataScience/tbats
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip-tools)
BuildRequires:  python3dist(pmdarima)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(rpy2)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)

%description
 BATS and TBATS time series forecastingPackage provides BATS and TBATS time
series forecasting methods described in:> De Livera, A.M., Hyndman, R.J., &
Snyder, R. D. (2011), Forecasting time series with complex seasonal patterns
using exponential smoothing, Journal of the American Statistical Association,
106(496), 1513-1527. InstallationFrom pypi:bash pip install tbats Import
via:python from...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(numpy)
Requires:       python3dist(pmdarima)
Requires:       python3dist(scikit-learn)
Requires:       python3dist(scipy)
%description -n python3-%{pypi_name}
 BATS and TBATS time series forecastingPackage provides BATS and TBATS time
series forecasting methods described in:> De Livera, A.M., Hyndman, R.J., &
Snyder, R. D. (2011), Forecasting time series with complex seasonal patterns
using exponential smoothing, Journal of the American Statistical Association,
106(496), 1513-1527. InstallationFrom pypi:bash pip install tbats Import
via:python from...


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
* Tue Mar 19 2024 Tim Lee - 1.1.3-1
- Initial package.
