%global pypi_name gym-notices
%global pypi_version 0.0.8

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Notices for gym

License:        None
URL:            https://github.com/Farama-Foundation/gym-notices
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Gym NoticesThis repository hosts notices for Gym that may be displayed on
import on internet connected systems, in order to give notices if versions have
major reproducibility issues, are very old and need to be upgraded (e.g.
there's been issues with researchers using 4 year old versions of Gym for no
reason), or other similar issues. If you're using a current version of Gym and
nothing...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 Gym NoticesThis repository hosts notices for Gym that may be displayed on
import on internet connected systems, in order to give notices if versions have
major reproducibility issues, are very old and need to be upgraded (e.g.
there's been issues with researchers using 4 year old versions of Gym for no
reason), or other similar issues. If you're using a current version of Gym and
nothing...


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
%doc README.md
%{python3_sitelib}/gym_notices
%{python3_sitelib}/gym_notices-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 16 2024 Tim Lee <timarthurlee@gmail.com> - 0.0.8-1
- Initial package.
