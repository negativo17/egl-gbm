Name:           egl-gbm
Epoch:          2
Version:        1.1.4
Release:        1%{?dist}
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
The GBM EGL external platform library.

%prep
%autosetup -p1

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
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%changelog
* Fri Sep 04 2026 Simone Caronni <negativo17@gmail.com> - 2:1.1.4-1
- Update to 1.1.4.

* Thu Jan 15 2026 Simone Caronni <negativo17@gmail.com> - 2:1.1.3-1
- Update to 1.1.3.

* Thu Mar 27 2025 Simone Caronni <negativo17@gmail.com> - 2:1.1.2.1-1
- Update to 1.1.2.1.
- Trim changelog.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.2^20240919gitb24587d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 20 2024 Simone Caronni <negativo17@gmail.com> - 2:1.1.2^20240919gitb24587d-3
- Update to latest snapshot.
- ICD is installed directly from source.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 2:1.1.2-2
- Add the library ICD (moved from egl-wayland).

* Tue Aug 13 2024 Simone Caronni <negativo17@gmail.com> - 2:1.1.2-1
- Update to final 1.1.2.

* Wed Aug 07 2024 Simone Caronni <negativo17@gmail.com> - 2:1.1.1-6.20240412git649c079
- Update to latest snapshot with required commits for driver 560+.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 28 2024 Leigh Scott <leigh123linux@gmail.com> - 2:1.1.1-4
- Add an epoch as some fool addded an epoch to their thirdparty repo!

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Leigh Scott <leigh123linux@gmail.com> - 1.1.1-1
- Update to 1.1.1
