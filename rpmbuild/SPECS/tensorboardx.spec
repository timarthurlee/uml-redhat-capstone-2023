%global pypi_name tensorboardx
%global pypi_version 2.6.2.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        TensorBoardX lets you watch Tensors Flow without Tensorflow

License:        MIT license
URL:            https://github.com/lanpa/tensorboardX
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/tensorboardX-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(protobuf) >= 3.20
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx)

%description
 2.6.2.1 (2023-08-20) * Added protobuf's lower bound version (>3.20)2.6.2
(2023-07-30) - * Removed version limit for protobuf2.6.1 (2023-06-18) - *
Expose use_strict_trace parameter in add_graph (694) * Upgrade to protobuf 4 *
Fix git based package versioning * Fix GCS Connection Error 606 (686)2.6
(2023-02-12) - * Fixed several deprecation warnings * Update dependencies2.5.1
(2022-06-05) - *...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(numpy)
Requires:       python3dist(packaging)
Requires:       python3dist(protobuf) >= 3.20
%description -n python3-%{pypi_name}
 2.6.2.1 (2023-08-20) * Added protobuf's lower bound version (>3.20)2.6.2
(2023-07-30) - * Removed version limit for protobuf2.6.1 (2023-06-18) - *
Expose use_strict_trace parameter in add_graph (694) * Upgrade to protobuf 4 *
Fix git based package versioning * Fix GCS Connection Error 606 (686)2.6
(2023-02-12) - * Fixed several deprecation warnings * Update dependencies2.5.1
(2022-06-05) - *...

%package -n python-%{pypi_name}-doc
Summary:        tensorboardx documentation
%description -n python-%{pypi_name}-doc
Documentation for tensorboardx

%prep
%autosetup -n tensorboardX-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/tensorboardX
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Mar 19 2024 Tim Lee - 2.6.2.2-1
- Initial package.
