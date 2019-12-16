#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : alembic
Version  : 1.3.2
Release  : 72
URL      : https://files.pythonhosted.org/packages/dc/6d/3c1411dfdcf089ec89ce5e2222deb2292f39b6b1a5911222e15af9fe5a92/alembic-1.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/6d/3c1411dfdcf089ec89ce5e2222deb2292f39b6b1a5911222e15af9fe5a92/alembic-1.3.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/dc/6d/3c1411dfdcf089ec89ce5e2222deb2292f39b6b1a5911222e15af9fe5a92/alembic-1.3.2.tar.gz.asc
Summary  : A open framework for storing and sharing scene data
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
BuildRequires : Mako
BuildRequires : Mako-python
BuildRequires : MarkupSafe
BuildRequires : SQLAlchemy
BuildRequires : buildreq-distutils3
BuildRequires : funcsigs
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : python-dateutil
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
%setup -q -n alembic-1.3.2
cd %{_builddir}/alembic-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576539992
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alembic
cp %{_builddir}/alembic-1.3.2/LICENSE %{buildroot}/usr/share/package-licenses/alembic/d3dffefa259626c91331ec5302d469864fc172ed
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
/usr/share/package-licenses/alembic/d3dffefa259626c91331ec5302d469864fc172ed

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
