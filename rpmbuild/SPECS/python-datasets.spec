%global pypi_name datasets
%global pypi_version 2.18.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        HuggingFace community-driven open-source library of datasets

License:        Apache 2.0
URL:            https://github.com/huggingface/datasets
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(absl-py)
BuildRequires:  python3dist(accelerate)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(apache-beam) >= 2.26
BuildRequires:  python3dist(bert-score) >= 0.3.6
BuildRequires:  (python3dist(dill) >= 0.3 with python3dist(dill) < 0.3.9~~)
BuildRequires:  python3dist(elasticsearch) < 8~~
BuildRequires:  python3dist(faiss-cpu) >= 1.6.4
BuildRequires:  python3dist(filelock)
BuildRequires:  (python3dist(fsspec) >= 2023.1 with python3dist(fsspec) <= 2024.2)
BuildRequires:  python3dist(huggingface-hub) >= 0.19.4
BuildRequires:  python3dist(jax) >= 0.3.14
BuildRequires:  python3dist(jaxlib) >= 0.3.14
BuildRequires:  python3dist(jiwer)
BuildRequires:  python3dist(joblib) < 1.3~~
BuildRequires:  python3dist(joblibspark)
BuildRequires:  python3dist(langdetect)
BuildRequires:  python3dist(librosa)
BuildRequires:  python3dist(lz4)
BuildRequires:  python3dist(mauve-text)
BuildRequires:  python3dist(multiprocess)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(numpy) >= 1.17
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pillow) >= 6.2.1
BuildRequires:  python3dist(py7zr)
BuildRequires:  python3dist(pyarrow) >= 12
BuildRequires:  python3dist(pyarrow-hotfix)
BuildRequires:  python3dist(pyspark) >= 3.4
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-datadir)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyyaml) >= 5.1
BuildRequires:  python3dist(rarfile) >= 4
BuildRequires:  python3dist(requests) >= 2.19
BuildRequires:  python3dist(requests-file) >= 1.5.1
BuildRequires:  python3dist(rouge-score)
BuildRequires:  python3dist(ruff) >= 0.3
BuildRequires:  python3dist(s3fs) >= 2021.11.1
BuildRequires:  python3dist(sacrebleu)
BuildRequires:  python3dist(sacremoses)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(sentencepiece)
BuildRequires:  python3dist(seqeval)
BuildRequires:  python3dist(setuptools)
BuildRequires:  (python3dist(six) >= 1.15 with python3dist(six) < 1.16)
BuildRequires:  python3dist(soundfile) >= 0.12.1
BuildRequires:  python3dist(spacy) >= 3
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  (python3dist(tensorflow) >= 2.2 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
BuildRequires:  (python3dist(tensorflow) >= 2.2 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
BuildRequires:  (python3dist(tensorflow) >= 2.2 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
BuildRequires:  (python3dist(tensorflow) >= 2.3 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
BuildRequires:  (python3dist(tensorflow) >= 2.3 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
BuildRequires:  python3dist(tensorflow) = 2.12
BuildRequires:  (python3dist(tensorflow-gpu) >= 2.2 with (python3dist(tensorflow-gpu) < 2.6.1 or python3dist(tensorflow-gpu) > 2.6.1) with (python3dist(tensorflow-gpu) < 2.6 or python3dist(tensorflow-gpu) > 2.6))
BuildRequires:  python3dist(tensorflow-macos)
BuildRequires:  python3dist(texttable) >= 1.6.3
BuildRequires:  python3dist(tiktoken)
BuildRequires:  python3dist(tldextract) >= 3.1
BuildRequires:  python3dist(toml) >= 0.10.1
BuildRequires:  python3dist(torch) >= 2
BuildRequires:  python3dist(tqdm) >= 4.62.1
BuildRequires:  python3dist(transformers) = 4.30.1
BuildRequires:  python3dist(typer) < 0.5~~
BuildRequires:  python3dist(typing-extensions) >= 4.6.1
BuildRequires:  python3dist(werkzeug) >= 1.0.1
BuildRequires:  python3dist(xxhash)
BuildRequires:  python3dist(zstandard)

%description
<p align"center"> <picture> <source media"(prefers-color-scheme: dark)" srcset"
<source media"(prefers-color-scheme: light)" srcset" <img alt"Hugging Face
Datasets Library" src" width"352" height"59" style"max-width: 100%;">
</picture> <br/> <p align"center"> <a href"

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(absl-py)
Requires:       python3dist(accelerate)
Requires:       python3dist(aiohttp)
Requires:       python3dist(apache-beam) >= 2.26
Requires:       python3dist(bert-score) >= 0.3.6
Requires:       (python3dist(dill) >= 0.3 with python3dist(dill) < 0.3.9~~)
Requires:       python3dist(elasticsearch) < 8~~
Requires:       python3dist(faiss-cpu) >= 1.6.4
Requires:       python3dist(filelock)
Requires:       (python3dist(fsspec) >= 2023.1 with python3dist(fsspec) <= 2024.2)
Requires:       python3dist(huggingface-hub) >= 0.19.4
Requires:       python3dist(jax) >= 0.3.14
Requires:       python3dist(jaxlib) >= 0.3.14
Requires:       python3dist(jiwer)
Requires:       python3dist(joblib) < 1.3~~
Requires:       python3dist(joblibspark)
Requires:       python3dist(langdetect)
Requires:       python3dist(librosa)
Requires:       python3dist(lz4)
Requires:       python3dist(mauve-text)
Requires:       python3dist(multiprocess)
Requires:       python3dist(nltk)
Requires:       python3dist(numpy) >= 1.17
Requires:       python3dist(packaging)
Requires:       python3dist(pandas)
Requires:       python3dist(pillow) >= 6.2.1
Requires:       python3dist(py7zr)
Requires:       python3dist(pyarrow) >= 12
Requires:       python3dist(pyarrow-hotfix)
Requires:       python3dist(pyspark) >= 3.4
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-datadir)
Requires:       python3dist(pytest-xdist)
Requires:       python3dist(pyyaml) >= 5.1
Requires:       python3dist(rarfile) >= 4
Requires:       python3dist(requests) >= 2.19
Requires:       python3dist(requests-file) >= 1.5.1
Requires:       python3dist(rouge-score)
Requires:       python3dist(ruff) >= 0.3
Requires:       python3dist(s3fs) >= 2021.11.1
Requires:       python3dist(sacrebleu)
Requires:       python3dist(sacremoses)
Requires:       python3dist(scikit-learn)
Requires:       python3dist(scipy)
Requires:       python3dist(sentencepiece)
Requires:       python3dist(seqeval)
Requires:       python3dist(setuptools)
Requires:       (python3dist(six) >= 1.15 with python3dist(six) < 1.16)
Requires:       python3dist(soundfile) >= 0.12.1
Requires:       python3dist(spacy) >= 3
Requires:       python3dist(sqlalchemy)
Requires:       (python3dist(tensorflow) >= 2.2 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
Requires:       (python3dist(tensorflow) >= 2.2 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
Requires:       (python3dist(tensorflow) >= 2.2 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
Requires:       (python3dist(tensorflow) >= 2.3 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
Requires:       (python3dist(tensorflow) >= 2.3 with (python3dist(tensorflow) < 2.6.1 or python3dist(tensorflow) > 2.6.1) with (python3dist(tensorflow) < 2.6 or python3dist(tensorflow) > 2.6))
Requires:       python3dist(tensorflow) = 2.12
Requires:       (python3dist(tensorflow-gpu) >= 2.2 with (python3dist(tensorflow-gpu) < 2.6.1 or python3dist(tensorflow-gpu) > 2.6.1) with (python3dist(tensorflow-gpu) < 2.6 or python3dist(tensorflow-gpu) > 2.6))
Requires:       python3dist(tensorflow-macos)
Requires:       python3dist(texttable) >= 1.6.3
Requires:       python3dist(tiktoken)
Requires:       python3dist(tldextract)
Requires:       python3dist(tldextract) >= 3.1
Requires:       python3dist(toml) >= 0.10.1
Requires:       python3dist(torch) >= 2
Requires:       python3dist(tqdm) >= 4.62.1
Requires:       python3dist(transformers) = 4.30.1
Requires:       python3dist(typer) < 0.5~~
Requires:       python3dist(typing-extensions) >= 4.6.1
Requires:       python3dist(werkzeug) >= 1.0.1
Requires:       python3dist(xxhash)
Requires:       python3dist(zstandard)
%description -n python3-%{pypi_name}
<p align"center"> <picture> <source media"(prefers-color-scheme: dark)" srcset"
<source media"(prefers-color-scheme: light)" srcset" <img alt"Hugging Face
Datasets Library" src" width"352" height"59" style"max-width: 100%;">
</picture> <br/> <p align"center"> <a href"


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
%doc README.md src/datasets/utils/readme.py src/datasets/utils/resources/readme_structure.yaml tests/test_readme_util.py
%{_bindir}/datasets-cli
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Mar 19 2024 Tim Lee - 2.18.0-1
- Initial package.
