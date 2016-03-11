#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : alembic
Version  : 0.8.5
Release  : 28
URL      : https://pypi.python.org/packages/source/a/alembic/alembic-0.8.5.tar.gz
Source0  : https://pypi.python.org/packages/source/a/alembic/alembic-0.8.5.tar.gz
Summary  : A database migration tool for SQLAlchemy.
Group    : Development/Tools
License  : MIT
Requires: alembic-bin
Requires: alembic-python
BuildRequires : Mako-python
BuildRequires : MarkupSafe-python
BuildRequires : SQLAlchemy-python
BuildRequires : funcsigs-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov-python
BuildRequires : python-dev
BuildRequires : python-editor
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Rudimentary multi-database configuration.

%package bin
Summary: bin components for the alembic package.
Group: Binaries

%description bin
bin components for the alembic package.


%package python
Summary: python components for the alembic package.
Group: Default
Requires: Mako-python
Requires: SQLAlchemy-python

%description python
python components for the alembic package.


%prep
%setup -q -n alembic-0.8.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/alembic

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
