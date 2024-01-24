%global pypi_name darts
%global pypi_version 0.27.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A python library for easy manipulation and forecasting of time series

License:        Apache License 2.0
URL:            https://unit8co.github.io/darts/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(holidays) >= 0.11.1
BuildRequires:  python3dist(joblib) >= 0.16
BuildRequires:  python3dist(matplotlib) >= 3.3
BuildRequires:  python3dist(nfoursid) >= 1
BuildRequires:  python3dist(numpy) >= 1.19
BuildRequires:  (python3dist(pandas) >= 1.0.5 with python3dist(pandas) < 2~~)
BuildRequires:  python3dist(pandas) >= 1.0.5
BuildRequires:  python3dist(pmdarima) >= 1.8
BuildRequires:  python3dist(pyod) >= 0.9.5
BuildRequires:  python3dist(pytorch-lightning) >= 1.5
BuildRequires:  python3dist(requests) >= 2.22
BuildRequires:  python3dist(scikit-learn) >= 1.0.1
BuildRequires:  python3dist(scipy) >= 1.3.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(shap) >= 0.40
BuildRequires:  python3dist(statsforecast) >= 1.4
BuildRequires:  python3dist(statsmodels) >= 0.14
BuildRequires:  python3dist(tbats) >= 1.1
BuildRequires:  python3dist(tensorboardx) >= 2.1
BuildRequires:  python3dist(torch) >= 1.8
BuildRequires:  python3dist(tqdm) >= 4.60
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(xarray) >= 0.17
BuildRequires:  python3dist(xgboost) >= 1.6

%description
 Time Series Made Easy in Python!

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(holidays) >= 0.11.1
Requires:       python3dist(joblib) >= 0.16
Requires:       python3dist(matplotlib) >= 3.3
Requires:       python3dist(nfoursid) >= 1
Requires:       python3dist(numpy) >= 1.19
Requires:       (python3dist(pandas) >= 1.0.5 with python3dist(pandas) < 2~~)
Requires:       python3dist(pandas) >= 1.0.5
Requires:       python3dist(pmdarima) >= 1.8
Requires:       python3dist(pyod) >= 0.9.5
Requires:       python3dist(pytorch-lightning) >= 1.5
Requires:       python3dist(requests) >= 2.22
Requires:       python3dist(scikit-learn) >= 1.0.1
Requires:       python3dist(scipy) >= 1.3.2
Requires:       python3dist(shap) >= 0.40
Requires:       python3dist(statsforecast) >= 1.4
Requires:       python3dist(statsmodels) >= 0.14
Requires:       python3dist(tbats) >= 1.1
Requires:       python3dist(tensorboardx) >= 2.1
Requires:       python3dist(torch) >= 1.8
Requires:       python3dist(tqdm) >= 4.60
Requires:       python3dist(typing-extensions)
Requires:       python3dist(xarray) >= 0.17
Requires:       python3dist(xgboost) >= 1.6
%description -n python3-%{pypi_name}
 Time Series Made Easy in Python![darts]( "darts") [![PyPI version]( [![Conda
Version]( ![Supported versions]( ![Docker Image Version (latest by date)](
![GitHub Release Date]( ![GitHub Workflow Status](


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
* Tue Dec 05 2023 Tim Lee - 0.27.0-1
- Initial package.