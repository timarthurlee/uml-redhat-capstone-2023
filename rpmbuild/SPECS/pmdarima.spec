%global pypi_name pmdarima
%global pypi_version 2.0.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python's forecast::auto.arima equivalent

License:        MIT
URL:            http://alkaline-ml.com/pmdarima
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(cython) >= 0.29 with (python3dist(cython) < 0.29.31 or python3dist(cython) > 0.29.31) with (python3dist(cython) < 0.29.18 or python3dist(cython) > 0.29.18))
BuildRequires:  python3dist(joblib) >= 0.11
BuildRequires:  python3dist(numpy) >= 1.21.2
BuildRequires:  python3dist(packaging) >= 17.1
BuildRequires:  python3dist(pandas) >= 0.19
BuildRequires:  python3dist(scikit-learn) >= 0.22
BuildRequires:  python3dist(scipy) >= 1.3.2
BuildRequires:  (python3dist(setuptools) >= 38.6 with (python3dist(setuptools) < 50 or python3dist(setuptools) > 50))
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(statsmodels) >= 0.13.2
BuildRequires:  python3dist(urllib3)

%description
 pmdarima[![PyPI version]( [![CircleCI]( [![Github Actions Status](
[![codecov]( ![Supported versions](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(cython) >= 0.29 with (python3dist(cython) < 0.29.31 or python3dist(cython) > 0.29.31) with (python3dist(cython) < 0.29.18 or python3dist(cython) > 0.29.18))
Requires:       python3dist(joblib) >= 0.11
Requires:       python3dist(numpy) >= 1.21.2
Requires:       python3dist(packaging) >= 17.1
Requires:       python3dist(pandas) >= 0.19
Requires:       python3dist(scikit-learn) >= 0.22
Requires:       python3dist(scipy) >= 1.3.2
Requires:       (python3dist(setuptools) >= 38.6 with (python3dist(setuptools) < 50 or python3dist(setuptools) > 50))
Requires:       python3dist(statsmodels) >= 0.13.2
Requires:       python3dist(urllib3)
%description -n python3-%{pypi_name}
 pmdarima[![PyPI version]( [![CircleCI]( [![Github Actions Status](
[![codecov]( ![Supported versions](


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
%doc README.md examples/README.txt examples/arima/README.txt examples/datasets/README.txt examples/model_selection/README.txt examples/preprocessing/README.txt examples/utils/README.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 20 2024 Tim Lee <timarthurlee@gmail.com> - 2.0.4-1
- Initial package.
