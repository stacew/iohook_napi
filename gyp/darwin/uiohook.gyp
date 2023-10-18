{
    "variables": {"openssl_fips": ""},
    "targets": [
        {
            "target_name": "uiohook",
            "type": "shared_library",
            "sources": [
                "libuiohook/include/uiohook.h",
                "libuiohook/src/logger.c",
                "libuiohook/src/logger.h",
                "libuiohook/src/darwin/input_helper.h",
                "libuiohook/src/darwin/input_helper.c",
                "libuiohook/src/darwin/input_hook.c",
                "libuiohook/src/darwin/post_event.c",
                "libuiohook/src/darwin/system_properties.c",
            ],
            "include_dirs": ["libuiohook/include", "libuiohook/src"],
            
            "link_settings": {
                "libraries": [
                    "-framework IOKit",
                    "-framework Carbon",
                    "-framework ApplicationServices",
                    "-lobjc",
                    "-Wl,-rpath,@executable_path/.",
                    "-Wl,-rpath,@loader_path/.",
                    "-Wl,-rpath,<!(pwd)/build/Release/",
                ]
            },
            
            "defines": [
                "USE_IOKIT=1",
                "USE_OBJC=1",
            ],
            "cflags": ["-std=c99"],
        }
    ],
}
