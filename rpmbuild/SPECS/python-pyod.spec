%global pypi_name pyod
%global pypi_version 1.1.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A Comprehensive and Scalable Python Library for Outlier Detection (Anomaly Detection)

License:        None
URL:            https://github.com/yzhao062/pyod
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 38.6

%description
Python Outlier Detection (PyOD) **Deployment & Documentation & Stats &
License** :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(joblib)
Requires:       python3dist(matplotlib)
Requires:       python3dist(numba) >= 0.51
Requires:       python3dist(numpy) >= 1.19
Requires:       python3dist(scikit-learn) >= 0.22
Requires:       python3dist(scipy) >= 1.5.1
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
Python Outlier Detection (PyOD) **Deployment & Documentation & Stats &
License** :target:


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 20 2024 Tim Lee <timarthurlee@gmail.com> - 1.1.3-1
- Initial package.
