#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : alembic
Version  : 1.0.5
Release  : 53
URL      : https://files.pythonhosted.org/packages/1c/65/b8e4f5b2f345bb13b5e0a3fddd892b0b3f0e8ad4880e954fdc6a50d00d84/alembic-1.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/65/b8e4f5b2f345bb13b5e0a3fddd892b0b3f0e8ad4880e954fdc6a50d00d84/alembic-1.0.5.tar.gz
Source99 : https://files.pythonhosted.org/packages/1c/65/b8e4f5b2f345bb13b5e0a3fddd892b0b3f0e8ad4880e954fdc6a50d00d84/alembic-1.0.5.tar.gz.asc
Summary  : A database migration tool for SQLAlchemy.
Group    : Development/Tools
License  : MIT
Requires: alembic-bin = %{version}-%{release}
Requires: alembic-license = %{version}-%{release}
Requires: alembic-python = %{version}-%{release}
Requires: alembic-python3 = %{version}-%{release}
Requires: Mako
Requires: SQLAlchemy
Requires: python-dateutil
Requires: python-editor
BuildRequires : Mako-python
BuildRequires : MarkupSafe
BuildRequires : SQLAlchemy
BuildRequires : buildreq-distutils3
BuildRequires : funcsigs
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : python-editor
BuildRequires : python-mock
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Configuration that reads from a Pylons project environment.

%package bin
Summary: bin components for the alembic package.
Group: Binaries
Requires: alembic-license = %{version}-%{release}

%description bin
bin components for the alembic package.


%package license
Summary: license components for the alembic package.
Group: Default

%description license
license components for the alembic package.


%package python
Summary: python components for the alembic package.
Group: Default
Requires: alembic-python3 = %{version}-%{release}

%description python
python components for the alembic package.


%package python3
Summary: python3 components for the alembic package.
Group: Default
Requires: python3-core

%description python3
python3 components for the alembic package.


%prep
%setup -q -n alembic-1.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543390052
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alembic
cp LICENSE %{buildroot}/usr/share/package-licenses/alembic/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/alembic

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alembic/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
