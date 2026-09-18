import os

from conan import ConanFile
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout
from conan.tools.build import check_min_cppstd


class AutodiffConan(ConanFile):
    name = "autodiff"
    # Keep in sync with the `project(autodiff VERSION ...)` call in CMakeLists.txt
    version = "1.1.2"

    license = "MIT"
    author = "Allan Leal"
    url = "https://github.com/64-B1T/autodiff"
    description = "automatic differentiation made easier for C++"
    topics = ("autodiff", "automatic-differentiation", "derivatives", "header-only")

    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    options = {"with_eigen": [True, False]}
    default_options = {"with_eigen": True}

    exports_sources = "autodiff/*.hpp", "LICENSE"

    def layout(self):
        basic_layout(self, src_folder=".")

    def requirements(self):
        if self.options.with_eigen:
            self.requires("eigen/3.4.0", transitive_headers=True)

    def package_id(self):
        self.info.clear()

    def validate(self):
        check_min_cppstd(self, 17)

    def package(self):
        copy(
            self,
            "*.hpp",
            src=os.path.join(self.source_folder, "autodiff"),
            dst=os.path.join(self.package_folder, "include", "autodiff"),
        )
        copy(
            self,
            "LICENSE",
            src=self.source_folder,
            dst=os.path.join(self.package_folder, "licenses"),
        )

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.set_property("cmake_file_name", "autodiff")
        self.cpp_info.set_property("cmake_target_name", "autodiff::autodiff")
        if self.options.with_eigen:
            self.cpp_info.defines = ["AUTODIFF_EIGEN_FOUND"]
