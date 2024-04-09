%global pypi_name lion-pytorch
%global pypi_version 0.1.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Lion Optimizer - Pytorch

License:        MIT
URL:            https://github.com/lucidrains/lion-pytorch
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(torch) >= 1.6
%description -n python3-%{pypi_name}



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
%doc README.md
%{python3_sitelib}/lion_pytorch
%{python3_sitelib}/lion_pytorch-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 09 2024 Tim Lee - 0.1.4-1
- Initial package.
