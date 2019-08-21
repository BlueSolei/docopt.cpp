from conans import ConanFile, CMake, tools


class DocoptConan(ConanFile):
    name = "docopt"
    version = "0.1"
    license = "MIT"
    author = "Vladimir Keleshev, vladimir@keleshev.com"
    url = "https://github.com/BlueSolei/docopt.cpp"
    description = "C++11 port of docopt"
    topics = ("docopt")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    scm = {
        "type": "git",
        "subfolder": "docopt",
        "url": "auto",
        "revision": "auto"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="docopt")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="docopt")
        self.copy("*docopt.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["docopt"]

