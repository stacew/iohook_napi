{
    "variables": {"openssl_fips": ""},
    "targets": [
        {
            "target_name": "iohook",
            "win_delay_load_hook": "true",
            "type": "loadable_module",
            "sources": ["src/iohook.cc", "src/iohook.h"],
            "dependencies": ["./uiohook.gyp:uiohook"],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                "libuiohook/include",
            ],
            
            "link_settings": {
                "libraries": [
                    "-Wl,-rpath,<!(node -e \"console.log('builds/' + process.env.gyp_iohook_runtime + '-v' + process.env.gyp_iohook_abi + '-' + process.env.gyp_iohook_platform + '-' + process.env.gyp_iohook_arch + '/build/Release')\")",
                    "-Wl,-rpath,<!(pwd)/build/Release/",
                ]
            },
            
            "defines": [
                "USE_XKBCOMMON",
                "NAPI_DISABLE_CPP_EXCEPTIONS",
            ],            
            "cflags": ["-std=c++14", "-fPIC", "-fexceptions"],
            "cxxflags": ["-fexceptions"],
            "cflags_cc": ["-fexceptions"],
            
            "configurations": {"Release": {}},
        }
    ],
}
