from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMakeToolchain, CMakeDeps
import os
import pathlib

class eCALConan(ConanFile):
    name = "ecal"
    settings = "os", "compiler", "arch", "build_type"
    license = "BSD-3-Clause"
    generators = "cmake_paths", "cmake_find_package"
    build_requires = "cmake/3.21.1"
    
    def build_requirements(self):
        self.build_requires("doxygen/1.9.1")
    
    def requirements(self):
        self.requires("hdf5/1.10.6")
        self.requires("protobuf/3.17.1")
        self.requires("libcurl/7.78.0")
        self.requires("qt/5.15.2")
        self.requires("spdlog/1.9.2")
        self.requires("tclap/1.2.4")
        self.requires("asio/1.19.2")
        self.requires("gtest/1.11.0")
        self.requires("tinyxml2/8.0.0")
        self.requires("simpleini/4.17")
        self.requires("termcolor/2.0.0")
        self.requires("fineftp/1.2.0")
        self.requires("steinwurf/6.0.0")
        self.requires("openssl/1.1.1l", override=True)
        
    def configure(self):
        if self.settings.os == "Windows":
            self.options["qt"].qtwinextras = True
        self.options["qt"].shared = True
