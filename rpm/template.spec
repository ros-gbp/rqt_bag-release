%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rqt-bag-plugins
Version:        0.5.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_bag_plugins package

License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-cairo
Requires:       python3-pillow
Requires:       python3-pillow-qt
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rqt-bag
Requires:       ros-noetic-rqt-gui
Requires:       ros-noetic-rqt-gui-py
Requires:       ros-noetic-rqt-plot
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag files.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Feb 19 2021 Mabel Zhang <mabel@openrobotics.org> - 0.5.1-1
- Autogenerated by Bloom

* Thu Nov 12 2020 Mabel Zhang <mabel@openrobotics.org> - 0.5.0-1
- Autogenerated by Bloom

* Fri Aug 21 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.15-1
- Autogenerated by Bloom

* Fri Aug 07 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.14-1
- Autogenerated by Bloom

* Tue Mar 17 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.13-1
- Autogenerated by Bloom

