%global pypi_name polars
%global pypi_version 0.19.19

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Blazingly fast DataFrame library

License:        MIT
URL:            https://github.com/pola-rs/polars
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin)

%description
 Polars: Blazingly fast DataFrames in Rust, Python, Node.js, R and SQL

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export RUSTFLAGS="%build_rustflags"
%py3_build

%install
%py3_install

%check
export RUSTFLAGS="%build_rustflags"
%tox / %pytest / %pyproject_check_import

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 05 2023 Tim Lee - 0.19.19
- Initial package.