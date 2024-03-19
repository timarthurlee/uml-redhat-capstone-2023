%global pypi_name shap
%global pypi_version 0.45.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A unified approach to explain the output of any machine learning model

License:        MIT License
URL:            None
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(catboost)
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(gpboost)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(jupyter)
BuildRequires:  python3dist(keras)
BuildRequires:  python3dist(lightgbm)
BuildRequires:  python3dist(lime)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(myst-parser) = 2
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(nbformat)
BuildRequires:  python3dist(nbsphinx) = 0.9.3
BuildRequires:  python3dist(ngboost)
BuildRequires:  python3dist(nlp)
BuildRequires:  python3dist(numba)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(opencv-python)
BuildRequires:  python3dist(packaging) > 20.9.0
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(protobuf) = 3.20.3
BuildRequires:  python3dist(pyod)
BuildRequires:  python3dist(pyspark)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mpl)
BuildRequires:  python3dist(pytest-mpl)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(sentencepiece)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(slicer) = 0.0.7
BuildRequires:  python3dist(sphinx) = 7.2.6
BuildRequires:  python3dist(sphinx-github-changelog) = 1.2.1
BuildRequires:  python3dist(sphinx-rtd-theme) = 2
BuildRequires:  python3dist(tensorflow)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(torch) = 2.2
BuildRequires:  python3dist(torchvision)
BuildRequires:  python3dist(tqdm) >= 4.27
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(xgboost)

%description
<p align"center"> <img src" width"800" />[![PyPI]( [![Conda]( ![License](
![Tests]( [![Binder]( [![Documentation Status](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(catboost)
Requires:       python3dist(cloudpickle)
Requires:       python3dist(datasets)
Requires:       python3dist(gpboost)
Requires:       python3dist(ipython)
Requires:       python3dist(ipython)
Requires:       python3dist(jupyter)
Requires:       python3dist(keras)
Requires:       python3dist(lightgbm)
Requires:       python3dist(lime)
Requires:       python3dist(matplotlib)
Requires:       python3dist(matplotlib)
Requires:       python3dist(myst-parser) = 2
Requires:       python3dist(nbconvert)
Requires:       python3dist(nbformat)
Requires:       python3dist(nbsphinx) = 0.9.3
Requires:       python3dist(ngboost)
Requires:       python3dist(nlp)
Requires:       python3dist(numba)
Requires:       python3dist(numpy)
Requires:       python3dist(numpydoc)
Requires:       python3dist(opencv-python)
Requires:       python3dist(packaging) > 20.9.0
Requires:       python3dist(pandas)
Requires:       python3dist(protobuf) = 3.20.3
Requires:       python3dist(pyod)
Requires:       python3dist(pyspark)
Requires:       python3dist(pytest)
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-mpl)
Requires:       python3dist(pytest-mpl)
Requires:       python3dist(requests)
Requires:       python3dist(scikit-learn)
Requires:       python3dist(scipy)
Requires:       python3dist(sentencepiece)
Requires:       python3dist(slicer) = 0.0.7
Requires:       python3dist(sphinx) = 7.2.6
Requires:       python3dist(sphinx-github-changelog) = 1.2.1
Requires:       python3dist(sphinx-rtd-theme) = 2
Requires:       python3dist(tensorflow)
Requires:       python3dist(torch)
Requires:       python3dist(torch) = 2.2
Requires:       python3dist(torchvision)
Requires:       python3dist(tqdm) >= 4.27
Requires:       python3dist(transformers)
Requires:       python3dist(transformers)
Requires:       python3dist(xgboost)
%description -n python3-%{pypi_name}
<p align"center"> <img src" width"800" />[![PyPI]( [![Conda]( ![License](
![Tests]( [![Binder]( [![Documentation Status](


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
* Tue Mar 19 2024 Tim Lee - 0.45.0-1
- Initial package.
