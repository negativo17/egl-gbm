Name:           egl-gbm
Version:        1.1.0
Release:        2%{?dist}
Summary:        Nvidia egl gbm libary

License:        MIT
URL:            https://github.com/NVIDIA/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  eglexternalplatform-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libgbm-devel

%description
Nvidia egl gbm libary

%prep
%autosetup

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
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.0-1
- Initial build
