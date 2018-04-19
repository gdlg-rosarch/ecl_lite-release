# Script generated with Bloom
pkgdesc="ROS - Libraries and utilities for embedded and low-level linux development."
url='http://www.ros.org/wiki/ecl_lite'

pkgname='ros-kinetic-ecl-lite'
pkgver='0.61.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-ecl-config'
'ros-kinetic-ecl-converters-lite'
'ros-kinetic-ecl-errors'
'ros-kinetic-ecl-io'
'ros-kinetic-ecl-sigslots-lite'
'ros-kinetic-ecl-time-lite'
)

conflicts=()
replaces=()

_dir=ecl_lite
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_lite $srcdir/ecl_lite
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

