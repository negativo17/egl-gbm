%global commit0 e5eee6058a812bce6df792c54efc484c4f15b6d1
%global date 20230420
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-gbm
Epoch:          1
Version:        1.1.0
Release:        4%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:        The GBM EGL external platform library
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %url/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  eglexternalplatform-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libgbm-devel

%description
The GBM EGL external platform library.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%meson
%meson_build

%install
%meson_install
# Delete unversioned .so
rm %{buildroot}%{_libdir}/libnvidia-egl-gbm.so

%files
%license COPYING
%{_libdir}/libnvidia-egl-gbm.so.1*

%changelog
* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:1.1.0-4.20230420gite5eee60
- Bump epoch.

* Thu Jun 08 2023 Simone Caronni <negativo17@gmail.com> - 1.1.0-3.20230420gite5eee60
- Update to latest snapshot (535.43.02).

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.0-1
- Initial build
