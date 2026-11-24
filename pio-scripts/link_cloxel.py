Import('env')
import os

# Links the precompiled Cloxel usermod (precompiled/libcloxel.a) into the firmware.
# --whole-archive keeps every part of it, also code that is only reached through
# callbacks; the libraries it uses (NimBLE, WLED itself) are resolved by the rest of the link.
library = os.path.join(env.subst("$PROJECT_DIR"), "precompiled", "libcloxel.a")
if not os.path.isfile(library):
    raise SystemExit("Cloxel relink kit: %s is missing" % library)
env.Append(LINKFLAGS=["-Wl,--whole-archive", library, "-Wl,--no-whole-archive"])
