%global pypi_name imageio-ffmpeg
%global pypi_version 0.4.9

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        FFMPEG wrapper for Python

License:        BSD-2-Clause
URL:            https://github.com/imageio/imageio-ffmpeg
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
FFMPEG wrapper for Python.Note that the platform-specific wheels contain the
binary executable of ffmpeg, which makes this package around 60 MiB in size. I
guess that's the cost for being able to read/write video files.For Linux users:
the above is not the case when installing via your Linux package manager (if
that is possible), because this package would simply depend on ffmpeg in that
case.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
FFMPEG wrapper for Python.Note that the platform-specific wheels contain the
binary executable of ffmpeg, which makes this package around 60 MiB in size. I
guess that's the cost for being able to read/write video files.For Linux users:
the above is not the case when installing via your Linux package manager (if
that is possible), because this package would simply depend on ffmpeg in that
case.


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
%doc README.md imageio_ffmpeg/binaries/README.md
%{python3_sitelib}/imageio_ffmpeg
%{python3_sitelib}/imageio_ffmpeg-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 09 2024 Tim Lee - 0.4.9-1
- Initial package.
