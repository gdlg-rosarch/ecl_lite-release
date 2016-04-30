Name:           ros-kinetic-ecl-sigslots-lite
Version:        0.61.4
Release:        2%{?dist}
Summary:        ROS ecl_sigslots_lite package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_sigslots_lite
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-ecl-config
Requires:       ros-kinetic-ecl-errors
Requires:       ros-kinetic-ecl-license
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-ecl-config
BuildRequires:  ros-kinetic-ecl-errors
BuildRequires:  ros-kinetic-ecl-license

%description
This avoids use of dynamic storage (malloc/new) and thread safety (mutexes) to
provide a very simple sigslots implementation that can be used for *very*
embedded development.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Apr 30 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-2
- Autogenerated by Bloom

* Sat Apr 23 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-1
- Autogenerated by Bloom

* Sat Apr 23 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-0
- Autogenerated by Bloom

