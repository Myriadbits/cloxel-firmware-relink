Import('env')
import os

# Links the precompiled Cloxel usermod (precompiled/libcloxel.a) into the firmware.
# --whole-archive keeps every part of it, also code that is only reached through
# callbacks; the libraries it uses (NimBLE, WLED itself) are resolved by the rest of the link.
# The path is relative to the project folder (where PlatformIO links), so that a folder name
# with spaces in it does not break the linker command.
LIBRARY = "precompiled/libcloxel.a"
if not os.path.isfile(os.path.join(env.subst("$PROJECT_DIR"), LIBRARY)):
    raise SystemExit("Cloxel relink kit: %s is missing" % LIBRARY)
env.Append(LINKFLAGS=["-Wl,--whole-archive", LIBRARY, "-Wl,--no-whole-archive"])
