#

rules = [
    {
        'name': 'alire',
        'source': 'Ada LIbrary REpository',
        'description': 'Ada LIbrary REpository (alire)',
        'systemDependencies':
        [
            'gprbuild: GNAT project build tool',
            'gprconfig_kb: GNAT project configuration knowledge base',
            'gnat: GNU Ada Compiler',
            'cc: Clang Compiler',
            'xmlada: XML/Ada an XML parser for Ada95',
        ],
        'world':
        [
            'gprbuild --relocate-build-tree={TARGET} -j0 -P alr_env',
        ]
    },
    {
        'name': 'gid',
        'source': 'Generic Image Decoder',
        'description': 'Genric Image Decoder for Ada (gid)',
        'systemDependencies':
        [
            'gprbuild: Ada LIbrary REpository',
        ],
        'world':
        [
            'gprbuild --relocate-build-tree={TARGET} -j0 -p -P gid -XGID_Build_Mode=Debug to_bmp',
            'gprbuild --relocate-build-tree={TARGET} -j0 -p -P gid -XGID_Build_Mode=Fast',
            'gprbuild --relocate-build-tree={TARGET} -j0 -p -P gid -XGID_Build_Mode=Smallest mini',
        ]
    },
    {
        'name': 'openglada',
        'source': 'OpenGL Ada',
        'description': 'OpenGL bindings for Ada (openglada)',
        'systemDependencies':
        [
            'alire: Ada LIbrary REpository',
            'GLFW: OpenGL, OpenES and Vulkan Development FrameWork',
            'FreeType: Text rendering library',
            'GID: Generic Image Decoder for BMP, GIF, JPEG, PNG, PNM (PBM, PGM, PPM) and TGA'
        ],
        'world':
        [
            'gprbuild --relocate-build-tree={TARGET} -p -XWindowing_System=x11 -Xmode=release opengl/opengl.gpr',
            'gprbuild --relocate-build-tree={TARGET} -p -XWindowing_System=x11 -Xmode=release opengl-glfw/opengl-glfw.gpr',
        ]
    }

]


