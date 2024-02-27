%global pypi_name pytorch-lightning
%global pypi_version 2.2.0.post0

Name:           python-%{pypi_name}
Version:        2.2.0.post0
Release:        1%{?dist}
Summary:        PyTorch Lightning is the lightweight PyTorch wrapper for ML researchers

License:        Apache-2.0
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bitsandbytes) = 0.41
BuildRequires:  python3dist(cloudpickle) >= 1.3
BuildRequires:  python3dist(coverage) = 7.3.1
BuildRequires:  python3dist(fastapi)
BuildRequires:  python3dist(gym) >= 0.17
BuildRequires:  python3dist(hydra-core) >= 1.0.5
BuildRequires:  python3dist(ipython) < 8.15~~
BuildRequires:  python3dist(jsonargparse) >= 4.26.1
BuildRequires:  python3dist(lightning-utilities) >= 0.8
BuildRequires:  python3dist(matplotlib) > 3.1.0
BuildRequires:  python3dist(omegaconf) >= 2.0.5
BuildRequires:  python3dist(onnx) >= 0.14
BuildRequires:  python3dist(onnxruntime) >= 0.15
BuildRequires:  python3dist(pandas) > 1.0
BuildRequires:  python3dist(psutil) < 5.9.6~~
BuildRequires:  python3dist(pytest) = 7.4
BuildRequires:  python3dist(pytest-cov) = 4.1
BuildRequires:  python3dist(pytest-random-order) = 1.1
BuildRequires:  python3dist(pytest-rerunfailures) = 12
BuildRequires:  python3dist(pytest-timeout) = 2.1
BuildRequires:  python3dist(requests) < 2.32~~
BuildRequires:  python3dist(rich) >= 12.3
BuildRequires:  python3dist(scikit-learn) > 0.22.1.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tensorboard) >= 2.9.1
BuildRequires:  python3dist(tensorboardx) >= 2.2
BuildRequires:  python3dist(torchmetrics) >= 0.10
BuildRequires:  python3dist(torchvision) >= 0.14
BuildRequires:  python3dist(uvicorn)
BuildRequires:  python3dist(wheel)

%description
<div align"center"><img src" width"400px">**The lightweight PyTorch wrapper for
high-performance AI research. Scale your models, not the
boilerplate.**_________
_____________________________________________________________<p align"center">
<a href" • <a href"key-features">Key Features</a> • <a href"how-to-use">How To
Use</a> • <a href" • <a href"examples">Examples</a> • <a...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(bitsandbytes) = 0.41
Requires:       python3dist(bitsandbytes) = 0.41
Requires:       python3dist(cloudpickle) >= 1.3
Requires:       python3dist(coverage) = 7.3.1
Requires:       (python3dist(deepspeed) >= 0.8.2 with python3dist(deepspeed) <= 0.9.3)
Requires:       (python3dist(deepspeed) >= 0.8.2 with python3dist(deepspeed) <= 0.9.3)
Requires:       (python3dist(deepspeed) >= 0.8.2 with python3dist(deepspeed) <= 0.9.3)
Requires:       (python3dist(deepspeed) >= 0.8.2 with python3dist(deepspeed) <= 0.9.3)
Requires:       python3dist(fastapi)
Requires:       python3dist(fsspec) >= 2022.5
Requires:       python3dist(gym) >= 0.17
Requires:       python3dist(gym) >= 0.17
Requires:       python3dist(hydra-core) >= 1.0.5
Requires:       python3dist(hydra-core) >= 1.0.5
Requires:       python3dist(ipython) < 8.15~~
Requires:       python3dist(ipython) < 8.15~~
Requires:       python3dist(jsonargparse) >= 4.26.1
Requires:       python3dist(jsonargparse) >= 4.26.1
Requires:       python3dist(lightning-utilities) >= 0.8
Requires:       python3dist(lightning-utilities) >= 0.8
Requires:       python3dist(lightning-utilities) >= 0.8
Requires:       python3dist(matplotlib) > 3.1.0
Requires:       python3dist(matplotlib) > 3.1.0
Requires:       python3dist(numpy) >= 1.17.2
Requires:       python3dist(omegaconf) >= 2.0.5
Requires:       python3dist(omegaconf) >= 2.0.5
Requires:       python3dist(onnx) >= 0.14
Requires:       python3dist(onnxruntime) >= 0.15
Requires:       python3dist(packaging) >= 20
Requires:       python3dist(pandas) > 1.0
Requires:       python3dist(psutil) < 5.9.6~~
Requires:       python3dist(pytest) = 7.4
Requires:       python3dist(pytest-cov) = 4.1
Requires:       python3dist(pytest-random-order) = 1.1
Requires:       python3dist(pytest-rerunfailures) = 12
Requires:       python3dist(pytest-timeout) = 2.1
Requires:       python3dist(pyyaml) >= 5.4
Requires:       python3dist(requests) < 2.32~~
Requires:       python3dist(requests) < 2.32~~
Requires:       python3dist(rich) >= 12.3
Requires:       python3dist(rich) >= 12.3
Requires:       python3dist(scikit-learn) > 0.22.1.0
Requires:       python3dist(tensorboard) >= 2.9.1
Requires:       python3dist(tensorboardx) >= 2.2
Requires:       python3dist(tensorboardx) >= 2.2
Requires:       python3dist(torch) >= 1.13
Requires:       python3dist(torchmetrics) >= 0.10
Requires:       python3dist(torchmetrics) >= 0.10
Requires:       python3dist(torchmetrics) >= 0.7
Requires:       python3dist(torchvision) >= 0.14
Requires:       python3dist(torchvision) >= 0.14
Requires:       python3dist(tqdm) >= 4.57
Requires:       python3dist(typing-extensions) >= 4.4
Requires:       python3dist(uvicorn)
%description -n python3-%{pypi_name}
<div align"center"><img src" width"400px">**The lightweight PyTorch wrapper for
high-performance AI research. Scale your models, not the
boilerplate.**_________
_____________________________________________________________<p align"center">
<a href" • <a href"key-features">Key Features</a> • <a href"how-to-use">How To
Use</a> • <a href" • <a href"examples">Examples</a> • <a...


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
%doc README.md src/pytorch_lightning/README.md
%{python3_sitelib}/lightning_fabric
%{python3_sitelib}/pytorch_lightning
%{python3_sitelib}/pytorch_lightning-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Feb 20 2024 Tim Lee <timarthurlee@gmail.com> - 2.2.0.^post0-1
- Initial package.
