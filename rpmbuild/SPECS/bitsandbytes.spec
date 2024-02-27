%global pypi_name bitsandbytes
%global pypi_version 0.42.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        k-bit optimizers and matrix multiplication routines

License:        MIT
URL:            https://github.com/TimDettmers/bitsandbytes
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(einops)
BuildRequires:  python3dist(lion-pytorch)

%description
 bitsandbytesThe bitsandbytes is a lightweight wrapper around CUDA custom
functions, in particular 8-bit optimizers, matrix multiplication (LLM.int8()),
and quantization functions.Resources: - [8-bit Optimizer Paper]( -- [Video]( --
[Docs]( [LLM.int8() Paper]( -- [LLM.int8() Software Blog Post]( -- [LLM.int8()
Emergent Features Blog Post]( TL;DR

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(scipy)
%description -n python3-%{pypi_name}
 bitsandbytesThe bitsandbytes is a lightweight wrapper around CUDA custom
functions, in particular 8-bit optimizers, matrix multiplication (LLM.int8()),
and quantization functions.Resources: - [8-bit Optimizer Paper]( -- [Video]( --
[Docs]( [LLM.int8() Paper]( -- [LLM.int8() Software Blog Post]( -- [LLM.int8()
Emergent Features Blog Post]( TL;DR


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
%{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 27 2024 Tim Lee - 0.42.0-1
- Initial package.
